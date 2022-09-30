import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        CREATE TABLE operation(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            account_id INTEGER NOT NULL, 
            created_at TEXT NOT NULL,
            FOREIGN KEY(account_id) REFERENCES account(id)
        );
    """
    cursor.execute(sql)
