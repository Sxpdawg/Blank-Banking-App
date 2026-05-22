# This is a test comment to verify the Git workflow.
import sqlite3

def get_db_connection():
    try:
        # Connect to a local file named banking.db
        connection = sqlite3.connect('banking.db')
        # Enable foreign key support
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None
