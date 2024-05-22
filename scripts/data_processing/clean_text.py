import psycopg2
import logging

logger = logging.getLogger(__name__)

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
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        logger.info('Database connection established successfully')

        return conn

    except Exception as e:
        logger.error("Failed to connect to the databse: %s", e)


def fetch_raw_data(conn: psycopg2.connect, table_name: str) -> list:
    """
    Fetch raw data from a specified PostgresSQL database, including all columns.

    Args:
        conn: A psycopg2 connection object.
        table_name (str): Name of the table to fetch data from.

    Returns:
        list: List of tuples containing the data from the table.
    """
    try:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table_name}')
        data = cur.fetchall()

        logger.info(f"Fetched {len(data)} rows from table {table_name}")

        return data

    except Exception as e:
        logger.error(f"Error fetching data from the table {table_name:} {e}")
        raise  # Re-raise the exception for handling in the calling function


def store_cleaned_data(conn: psycopg2.connect, table_name: str, cleaned_data):
    """
    Store cleaned data and all other columns from the source data in the PostgresSQL database.

    Args:
        conn: A psycopg2 connection object.
        table_name (str): Name of the table to store cleaned data.
        cleaned_data (list): List of lists representing cleaned documents and their original data.
    """
    try:
        cur = conn.cursor()

        column_names = [row[1] for row in cur.description]

        placeholder_list = ', '.join(['%s' for _ in column_names])
        insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholder_list})"

        cur.executemany(insert_query, cleaned_data)
        conn.commit()
        logger.info(f"Stored {len(cleaned_data)} cleaned documents with original data into the table {table_name}.")

    except Exception as e:
        logger.error(f'Error storing cleaned data into table {table_name}: {e}')