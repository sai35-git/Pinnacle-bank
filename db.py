import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Accounts Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY,
            account_number VARCHAR(20) UNIQUE NOT NULL,
            holder_name VARCHAR(100) NOT NULL,
            balance NUMERIC(12, 2) DEFAULT 0.00,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 2. Transactions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            account_number VARCHAR(20) REFERENCES accounts(account_number),
            transaction_type VARCHAR(10) NOT NULL, -- 'DEPOSIT' or 'WITHDRAW'
            amount NUMERIC(12, 2) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    print("✅ Tables ('accounts' and 'transactions') initialized successfully!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()