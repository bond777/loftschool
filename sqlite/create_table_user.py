import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            phone TEXT NOT NULL UNIQUE,
            created_at TEXT
        );
    """
    cursor.execute(sql)
