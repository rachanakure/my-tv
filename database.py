# Create a database schema (e.g., create a file called `database.py`)
import sqlite3

def create_connection():
    connection = sqlite3.connect('users.db')
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Run this function to create the table
create_table()
