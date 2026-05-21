import sqlite3
from db import get_db_connection

def register_user(username, password_hash, email):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
            (username, password_hash, email)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print("Error: Username or Email already exists.")
        return None
    finally:
        conn.close()

def create_account(user_id, account_type):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (user_id, account_type) VALUES (?, ?)",
            (user_id, account_type)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()

def get_balance(account_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()

def transfer_funds(from_acc, to_acc, amount):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # Check sufficient funds
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_acc,))
        balance = cursor.fetchone()[0]
        if balance < amount:
            print("Insufficient funds")
            return False
        
        # Perform transfer inside a transaction
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_acc))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_acc))
        cursor.execute("INSERT INTO transactions (from_account_id, to_account_id, amount) VALUES (?, ?, ?)", (from_acc, to_acc, amount))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Transaction failed: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_transaction_history(account_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE from_account_id = ? OR to_account_id = ?", (account_id, account_id))
        return cursor.fetchall()
    finally:
        conn.close()

def delete_account(account_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()
