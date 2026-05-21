import sqlite3

conn = sqlite3.connect('banking.db')
cursor = conn.cursor()
cursor.execute("UPDATE accounts SET balance = 100 WHERE account_id = 1")
cursor.execute("INSERT INTO accounts (user_id, account_type) VALUES (1, 'checking')")
conn.commit()
conn.close()
print("Setup complete.")
