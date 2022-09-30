import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        DROP TABLE IF EXISTS user;
    """
    cursor.execute(sql)
