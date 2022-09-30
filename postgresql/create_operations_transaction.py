from postgresql.connection import connection
from datetime import datetime


with connection.cursor() as cursor:
    user_name = 'Гарри Поттер'
    cursor.execute('select id from "user" where name = %s', (user_name, ))
    user_id = cursor.fetchone()[0]

    account_name = 'Пластиковая карта'
    cursor.execute('select id from account where user_id = %s and name = %s', (user_id, account_name))
    account_id = cursor.fetchone()[0]
    amount = 100000

    cursor.execute('BEGIN;')
    sql = """
        insert into operation
            (amount, account_id, created_at)
        VALUES
            (%s , %s, %s)
    """
    cursor.execute(sql, (amount, account_id, datetime.now().isoformat()))

    sql = """
        update account set balance = balance + %s where id = %s
    """
    cursor.execute(sql, (amount, account_id))
    cursor.execute('COMMIT;')
