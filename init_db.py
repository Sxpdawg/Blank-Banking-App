import sqlite3
from db import get_db_connection

def create_tables():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        
        # SQLite schema
        schema = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            account_type TEXT CHECK(account_type IN ('savings', 'checking')) NOT NULL,
            balance DECIMAL(15, 2) DEFAULT 0.00,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_account_id INTEGER NOT NULL,
            to_account_id INTEGER NOT NULL,
            amount DECIMAL(15, 2) NOT NULL,
            memo TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (from_account_id) REFERENCES accounts(account_id),
            FOREIGN KEY (to_account_id) REFERENCES accounts(account_id)
        );
        """
        cursor.executescript(schema)
        conn.commit()
        conn.close()
        print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
