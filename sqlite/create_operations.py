import sqlite3
from datetime import datetime


with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    user_name = 'Гарри Поттер'
    res = cursor.execute('select id from user where name = ?', (user_name, ))
    user_id = res.fetchone()[0]

    account_name = 'Пластиковая карта'
    res = cursor.execute('select id from account where user_id = ? and name = ?', (user_id, account_name))
    account_id = res.fetchone()[0]
    amount = 100000

    sql = """
        insert into operation
            (amount, account_id, created_at)
        VALUES
            (? , ?, ?)
    """
    cursor.execute(sql, (amount, account_id, datetime.now().isoformat()))

    sql = """
        update account set balance = balance + ? where id = ?
    """
    cursor.execute(sql, (amount, account_id))
