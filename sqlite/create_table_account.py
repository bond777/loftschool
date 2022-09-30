import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        CREATE TABLE account(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL, 
            balance REAL NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """
    cursor.execute(sql)
