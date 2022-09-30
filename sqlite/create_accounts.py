import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    user_name = 'Гарри Поттер'
    res = cursor.execute('select id from user where name = ?', (user_name, ))
    user_id = res.fetchone()[0]

    sql = """
        insert into account
            (user_id, name, balance)
        VALUES
            (? , ?, ?)
    """
    cursor.execute(sql, (user_id, 'Пластиковая карта', 0))
