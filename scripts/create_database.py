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

    # List of required tables
    required_tables = ['News', 'Lyrics', 'Facebook']

    # Check existing tables
    cursor.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    existing_tables = [row[0] for row in cursor.fetchall()]

    # Filter out tables that need to be created
    tables_to_create = [table for table in required_tables if table not in existing_tables]

    if tables_to_create:
        with open('scripts/schema.sql', 'r') as schema_file:
            script = schema_file.read()
            cursor.execute(script)
        conn.commit()
        
    cursor.close()
    conn.close()


