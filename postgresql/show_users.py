from postgresql.connection import connection

with connection.cursor() as cursor:
    sql = 'select * from "user"'
    cursor.execute(sql)
    for user in cursor.fetchall():
        print(user)

