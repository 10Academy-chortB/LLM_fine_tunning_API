from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.env')
load_dotenv(env_path)

# Function to establish database connection
def connect_to_database():
    """Establishes a connection to the PostgreSQL database."""
    db_name = os.getenv('DB_NAME_CLEAN')
    port = os.getenv('PORT')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    user = os.getenv('USER_NAME')
    
    conn = psycopg2.connect(host=host, database=db_name, user=user, password=password, port=port)
    return conn

# Initialize Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    """Welcome message for the NP data API."""
    return "Welcome to the NP data API!"

# Route to fetch unique news sources
@app.route('/unique_source', methods=['GET'])
def get_source():
    """Fetches unique news sources from the database."""
    conn = connect_to_database()
    cur = conn.cursor()

    query = """
    SELECT DISTINCT "Source"
    FROM scrape.News    
    """
    cur.execute(query)
    rows = cur.fetchall()

    sources = [row[0] for row in rows]
    conn.close()
    return jsonify(sources), 200

# Route to fetch latest news
@app.route('/latest_news', methods=['GET'])
def get_news():
    """Fetches the latest news from the database."""
    conn = connect_to_database()
    cur = conn.cursor()

    query = """
    SELECT "Content"
    FROM scrape.News
    LIMIT 10
    """

    cur.execute(query)
    rows = cur.fetchall()

    news = [row[0] for row in rows]
    conn.close()
    return jsonify(news), 200

# Route to fetch unique artists
@app.route('/unique_artist', methods=['GET'])
def get_artist():
    """Fetches unique artists from the database."""
    conn = connect_to_database()
    cur = conn.cursor()

    query = """
    SELECT DISTINCT artist
    FROM scrape.Lyrics    
    """
    cur.execute(query)
    rows = cur.fetchall()

    artists = [row[0] for row in rows]
    conn.close()
    return jsonify(artists), 200

# Route to search news based on keyword
@app.route('/news_search', methods=['GET'])
def search_news():
    """Searches news based on a provided keyword."""
    conn = connect_to_database()
    cur = conn.cursor()

    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword in search query"}), 400
    
    query = """
    SELECT * FROM scrape.News
    WHERE "Headline" ILIKE %s OR "Content" ILIKE %s
    """

    cur.execute(query, (keyword, keyword))
    rows = cur.fetchall()
    conn.close()

    return jsonify(rows)


# Route to search lyrics based on keyword
@app.route('/lyrics_search', methods=['GET'])
def search_lyrics():
    """Searches lyrics based on a provided keyword."""
    conn = connect_to_database()
    cur = conn.cursor()

    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword in search query"}), 400
    
    query = """
    SELECT * FROM scrape.Lyrics
    WHERE "song_name" ILIKE %s
    """

    cur.execute(query, ('%' + keyword + '%',))
    rows = cur.fetchall()
    conn.close()

    return jsonify(rows)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
