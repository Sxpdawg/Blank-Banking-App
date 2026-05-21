from db import get_db_connection

conn = get_db_connection()
if conn:
    print("Successfully connected to the SQLite database!")
    conn.close()
else:
    print("Failed to connect to the database.")
