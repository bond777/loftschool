import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        select * from user
    """
    res = cursor.execute(sql)
    for user in res.fetchall():
        print(user)
