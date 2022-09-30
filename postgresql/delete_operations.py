from postgresql.connection import connection
from datetime import datetime


with connection.cursor() as cursor:

    operation_id = 1
    cursor.execute('BEGIN;')
    sql = 'select amount, account_id from operation where id = %s'
    cursor.execute(sql, (operation_id, ))
    (amount, account_id) = cursor.fetchone()
    
    sql = 'delete from operation where id = %s'
    cursor.execute(sql, (operation_id, ))
    sql = 'update account set balance = balance - %s where id = %s'
    cursor.execute(sql, (amount, account_id))
    cursor.execute('COMMIT;')
