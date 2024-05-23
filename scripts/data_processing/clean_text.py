from database_operations import get_db_connection, fetch_raw_data, store_cleaned_data
from preprocess import clean_document
import os
from dotenv import load_dotenv
from pathlib import Path


def main(raw_db_params, raw_table_name, clean_db_params, clean_table_name):
    """
    Process raw data and store the cleaned data in PostgreSQL database.

    Args:
        raw_db_params (dict): Parameters for the raw data database connection.
        raw_table_name (str): Table name of the raw data.
        clean_db_params (dict): Parameters for the cleaned data database connection.
        clean_table_name (str): Table name of the cleaned data.
    """

    raw_conn = get_db_connection(**raw_db_params)
    clean_conn = get_db_connection(** clean_db_params)

    raw_data = fetch_raw_data(raw_conn, raw_table_name)

    clean_data = [(doc[0], clean_document(doc[1]), doc[2], doc[3]) for doc in raw_data]

    store_cleaned_data(clean_conn, clean_table_name, clean_data)


    raw_conn.close()
    clean_conn.close()


if __name__ == "__main__":

    env_path = Path('.env')
    load_dotenv(env_path)

    raw_db_params = {
    'db_name' : os.getenv('DB_NAME_RAW'),
    'user' : os.getenv('USER_NAME'),
    'password' : os.getenv('PASSWORD'),
    'host' : os.getenv('HOST'),
    'port' : os.getenv('PORT')
    }

    clean_db_params = {
    'db_name' : os.getenv('DB_NAME_CLEAN'),
    'user' : os.getenv('USER_NAME'),
    'password' : os.getenv('PASSWORD'),
    'host' : os.getenv('HOST'),
    'port' : os.getenv('PORT')
    }

    raw_table_name = 'news'
    clean_table_name = 'news'

    main(raw_db_params, raw_table_name, clean_db_params, clean_table_name)



    
