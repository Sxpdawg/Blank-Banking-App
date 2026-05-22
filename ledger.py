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
        raise ValueError("Username or Email already exists.")
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
        if result is None:
            raise ValueError("Account not found.")
        return result[0]
    finally:
        conn.close()

def transfer_funds(from_acc, to_acc, amount, memo=None):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # Check sufficient funds
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_acc,))
        result = cursor.fetchone()
        if result is None:
            raise ValueError("Source account not found.")
        
        balance = result[0]
        if balance < amount:
            raise ValueError("Insufficient funds.")
        
        # Perform transfer inside a transaction
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_acc))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_acc))
        cursor.execute("INSERT INTO transactions (from_account_id, to_account_id, amount, memo) VALUES (?, ?, ?, ?)", (from_acc, to_acc, amount, memo))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Transaction failed: {e}")
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
