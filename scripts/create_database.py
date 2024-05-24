import psycopg2
from psycopg2 import sql
from pathlib import Path

def execute_schema(host, db_name, user, password, port) -> None:
    """
    Main function to load environment variables, establish a connection to the PostgreSQL database,
    read and execute the schema SQL script, and close the database connection.
    """
    
    conn = psycopg2.connect(host=host, database=db_name, user=user, password=password, port=port)
    cursor = conn.cursor()
    
    with open('scripts/schema.sql', 'r') as schema_file:
        script = schema_file.read()
        cursor.execute(script)
    
    conn.commit()
    cursor.close()
    conn.close()


