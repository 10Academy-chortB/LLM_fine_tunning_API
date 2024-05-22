import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
from pathlib import Path

def main() -> None:
    """
    Main function to load environment variables, establish a connection to the PostgreSQL database,
    read and execute the schema SQL script, and close the database connection.
    """
    env_path = Path('.env')
    load_dotenv(env_path)
    
    db_name: str = os.getenv('DB_NAME')
    port: str = os.getenv('PORT')
    password: str = os.getenv('PASSWORD')
    host: str = os.getenv('HOST')
    user: str = os.getenv('USER_NAME')
    
    conn = psycopg2.connect(host=host, database=db_name, user=user, password=password, port=port)
    cursor = conn.cursor()
    
    with open('scripts/schema.sql', 'r') as schema_file:
        script: str = schema_file.read()
        cursor.execute(script)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
