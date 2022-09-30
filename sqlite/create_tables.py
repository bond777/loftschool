import sqlite3


with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()

    # удаление таблицы user
    sql = """
        DROP TABLE IF EXISTS user;
    """
    cursor.execute(sql)

    # создание таблицы user
    sql = """
        CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128) NOT NULL, 
            phone VARCHAR(11) NOT NULL UNIQUE
        );
    """
    cursor.execute(sql)

    # удаление таблицы account
    sql = """
        DROP TABLE IF EXISTS account;
    """
    cursor.execute(sql)

    # создание таблицы account
    sql = """
        CREATE TABLE account(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name VARCHAR(128) NOT NULL, 
            balance REAL NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """
    cursor.execute(sql)

    # удаление таблицы operation
    sql = """
        DROP TABLE IF EXISTS operation;
    """
    cursor.execute(sql)

    # создание таблицы operation
    sql = """
        CREATE TABLE operation(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128) NOT NULL,
            created_at 
            user_id INTEGER NOT NULL,
            name VARCHAR(128) NOT NULL, 
            balance REAL NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """
    cursor.execute(sql)