import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_database import execute_schema



def main() -> None:
    """
    Main function to load environment variables, establish a connection to the PostgreSQL database,
    read and execute the schema SQL script, and close the database connection.
    """
    env_path = Path('.env')
    load_dotenv(env_path)
    
    db_name = os.getenv('DB_NAME_CLEAN')
    port = os.getenv('PORT')
    password= os.getenv('PASSWORD')
    host= os.getenv('HOST')
    user = os.getenv('USER_NAME')
    
    execute_schema(host, db_name, user, password, port) 

if __name__ == "__main__":
    main()
