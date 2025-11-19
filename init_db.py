import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("SUPABASE_DB_URL")

def init_database():
    """Initialize database with tables"""
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Read and execute schema
    with open('schema.sql', 'r') as f:
        schema_sql = f.read()
    
    cursor.execute(schema_sql)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_database()
