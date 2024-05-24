import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import logging
from pathlib import Path
from telethon import TelegramClient

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

filehandler = logging.FileHandler('logs/raw.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

def scrape_news_page(base_url, num_pages, title_selector, article_selector, content_selector, class_selector, date_selector) -> None:
    """
    Scrapes news articles from the specified base URL and saves the data to a database.

    Args:
        base_url (str): The base URL of the news site.
        num_pages (int): The number of pages to scrape.
        title_selector (str): The CSS selector for the article titles.
        article_selector (str): The CSS selector for the article links.
        content_selector (str): The CSS selector for the article content.
        class_selector (str): The CSS class for the article content container.
        date_selector (str): The CSS selector for the article date.
    """
    try:
        url_page = base_url + '?page={}'

        for page_num in range(1, num_pages+1):
            url = url_page.format(page_num)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = soup.find_all(title_selector)

            for headline in headlines:
                headlines_text = headline.get_text()
                article_link = headline.find(article_selector)['href']
                article_response = requests.get(article_link)
                article_soup = BeautifulSoup(article_response.content, 'html.parser')
                article_body = article_soup.find(class_=class_selector)
                bodies = article_body.find_all(content_selector)
                article_body_text = ''.join(body.get_text() for body in bodies)
                date = soup.find(date_selector)
                date_text = date.get_text()
                save_to_db('scrape.News', headlines_text, article_body_text, base_url, date_text)

        logger.info('Succesfully loaded the {base_url} into postgres')
    except Exception as e:
        logger.error('Error loading the {base_url} into postgres database : {e}')
        

def scrape_news_more(base_url, more_button_selector, title_selector, content_selector, article_link_selector, date_selector) -> None:
    """
    Scrapes additional news articles from the specified base URL using a "more" button.

    Args:
        base_url (str): The base URL of the news site.
        more_button_selector (str): The CSS selector for the "more" button.
        title_selector (str): The CSS selector for the article titles.
        content_selector (str): The CSS selector for the article content.
        article_link_selector (str): The CSS selector for the article links.
        date_selector (str): The CSS selector for the article date.
    """
    try:
        session = requests.Session()
        scraped_urls = set()
        url = base_url

        while url:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.select(article_link_selector)

            for article in articles:
                article_url = article.get('href')
                if not article_url or article_url in scraped_urls:
                    continue

                # Add the domain if the URL is relative
                if article_url.startswith('/'):
                    article_url = f"{base_url.rstrip('/')}{article_url}"

                scraped_urls.add(article_url)
                article_response = session.get(article_url)
                article_soup = BeautifulSoup(article_response.text, 'html.parser')
                title = article.get_text(strip=True)
                date_element = article_soup.select_one(date_selector)
                date = date_element.get_text(strip=True) if date_element else 'Unknown date'
                bodies = article_soup.select(content_selector)
                content = ''.join(body.get_text(strip=True) for body in bodies)
                save_to_db('scrape.News', title, content, article_url, date)

            more_button = soup.select_one(more_button_selector)
            if more_button:
                next_page = more_button.get('href')
                url = f"{base_url.rstrip('/')}{next_page}" if next_page.startswith('/') else next_page
            else:
                url = None

        logger.info('Succesfully loaded the {base_url} into postgres')
    except Exception as e:
        logger.error('Error loading the {base_url} into postgres database : {e}')

def scrape_telegram(channel_username: str, url: str) -> None:
    """
    Scrapes messages from a specified Telegram channel and saves the data to a database.

    Args:
        channel_username (str): The username of the Telegram channel.
        url (str): The URL of the Telegram channel.
    """
    try:
        env_path = Path('.env')
        load_dotenv(env_path)
        api_id = os.getenv('api_id')
        api_hash = os.getenv('api_hash')
        phone = os.getenv('phone')
        client = TelegramClient(channel_username, api_id, api_hash)

        async def main() -> None:
            await client.start()
            entity = await client.get_entity(channel_username)
            async for message in client.iter_messages(entity):
                save_to_db('scrape.News', channel_username, message.message, url, message.date)

        with client:
            client.loop.run_until_complete(main())

        logger.info('Succesfully loaded the {channel_username} into postgres')
    except Exception as e:
        logger.error('Error loading the {channel_username} into postgres database : {e}')



def save_to_db(table: str, title: str, content: str, source: str, date: str) -> None:
    """
    Saves the scraped data to a PostgreSQL database.

    Args:
        table (str): The name of the table to insert data into.
        title (str): The title of the article or message.
        content (str): The content of the article or message.
        source (str): The source URL of the article or message.
        date (str): The date of the article or message.
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

    cur.execute(f"INSERT INTO {table} VALUES (%s, %s, %s, %s)", (title, content, source, date))

    conn.commit()
    cur.close()
    conn.close()
