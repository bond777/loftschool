from postgresql.connection import connection

with connection.cursor() as cursor:
    user_name = 'Гарри Поттер'
    res = cursor.execute('select id from "user" where name = %s', (user_name, ))
    user_id = cursor.fetchone()[0]

    sql = """
        insert into account
            (user_id, name, balance)
        VALUES
            (%s , %s, %s)
    """
    cursor.execute(sql, (user_id, 'Пластиковая карта', 0))

