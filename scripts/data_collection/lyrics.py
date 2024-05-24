import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import logging
from pathlib import Path


logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

filehandler = logging.FileHandler('logs/raw.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

def scrape_and_store(url: str, base_url: str, table: str) -> None:
    """
    Scrapes artist and song data from the specified URL and stores it in the database.

    Args:
        url (str): The URL to scrape.
        base_url (str): The base URL for relative links.
        table (str): The name of the table to insert data into.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        artists = soup.select('ol li a')

        for artist in artists:
            artist_name = artist.get_text()
            artist_url = base_url + artist['href']

            artist_response = requests.get(artist_url)
            artist_soup = BeautifulSoup(artist_response.content, 'html.parser')

            song_names = artist_soup.select('dl dd a')
            song_durations = artist_soup.select('dl dd span')

            for song_name, song_duration in zip(song_names, song_durations):
                song_title = song_name.get_text()
                song_url = base_url + song_name['href']
                duration = song_duration.get_text() if song_duration else 'Unknown duration'

                song_response = requests.get(song_url)
                song_soup = BeautifulSoup(song_response.content, 'html.parser')

                song_lyrics_div = song_soup.find('div', class_='poem')

                if song_lyrics_div:
                    song_lyrics = song_lyrics_div.get_text(separator="\n", strip=True)
                else:
                    song_lyrics = 'Lyrics not found'

                save_to_db(f'scrape.{table}', artist_name, song_title, song_lyrics, duration)

        logger.info(f'Successfully scraped and stored data from {url}.')
    except Exception as e:
        logger.error(f'Error scraping data from {url}: {e}')



def save_to_db(table: str, artist: str, song_name: str, lyrics: str, duration: str) -> None:
    """
    Saves the scraped data to a PostgreSQL database.

    Args:
        table (str): The name of the table to insert data into.
        artist (str): The name of the artist.
        song_name (str): The name of the song.
        lyrics (str): The lyrics of the song.
        duration (str): The duration of the song.
    """

    env_path = Path('.env')
    load_dotenv(env_path)

    db_name = os.getenv('DB_NAME_RAW')
    port = os.getenv('PORT')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    user = os.getenv('USER_NAME')
    conn = psycopg2.connect(host=host, database=db_name, user=user, password=password, port=port)
    cur = conn.cursor()

    cur.execute(
        f"INSERT INTO {table} (artist, song_name, lyrics, duration) VALUES (%s, %s, %s, %s)",
        (artist, song_name, lyrics, duration)
    )

    conn.commit()
    cur.close()
    conn.close()
    logger.info(f'Successfully inserted song "{song_name}" by artist "{artist}" with duration "{duration}" into the database.')
