import psycopg2
from psycopg2 import sql
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

filehandler = logging.FileHandler('logs/preprocessing.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)


def get_db_connection(db_name, user, password, host, port):
    """
    Returns connection
    """
    try:

        conn = psycopg2.connect(
            dbname = db_name,
            user = user,
            password = password,
            host = host,
            port = port
        )

        logger.info('Database connection established {db_name} successfully')

        return conn

    except Exception as e:
        logger.error("Failed to connect to the databse: %s", e)

       


def fetch_raw_data(conn: str, table_name: str) -> list:
    """
    Fetch raw data from a specified PostgresSQL database.


    Args:
        conn: A psycopg2 connection object.
        table_name (str): Name of the table to fetch data from.

    Returns:
        list: List of tuples contaning the data from the table.
    """
        
    try:
        with conn.cursor() as cursor:
            query = sql.SQL("SELECT * FROM scrape.{}").format(sql.Identifier(table_name))
            cursor.execute(query)
            data = cursor.fetchall()

            logger.info(f"Fetched {len(data)} rows from table {table_name}")

            return data
        
    except Exception as e:
        logger.error(f"Error fetching data from the table {table_name:} {e}")


def store_cleaned_data(conn, table_name, cleaned_data):
    """
    Create a new table and store cleaned data in the PostgreSQL database.

    Args:
        conn: A psycopg2 connection object.
        table_name (str): Name of the table to store cleaned data.
        cleaned_data (list): List of cleaned documents to be stored.
    """
    try:
        with conn.cursor() as cursor:
            for doc in cleaned_data:
                cursor.execute(
                    sql.SQL('INSERT INTO scrape.{} ("Headline", "Content", "Source", "date") VALUES (%s, %s, %s, %s)').format(sql.Identifier(table_name)),
                    doc  # Unpacking the tuple directly here
                )
        conn.commit()
        logger.info(f"Stored {len(cleaned_data)} cleaned documents into the table {table_name}.")
    except Exception as e:
        logger.error(f'Error storing cleaned data into table {table_name}: {e}')
