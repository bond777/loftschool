import sqlite3
from datetime import datetime


with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    operation_id = 1
    cursor.execute('BEGIN TRANSACTION;')
    sql = 'select amount, account_id from operation where id = ?'
    res = cursor.execute(sql, (operation_id, ))
    (amount, account_id) = res.fetchone()

    sql = 'delete from operation where id = ?'
    cursor.execute(sql, (operation_id, ))
    sql = 'update account set balance = balance - ? where id = ?'
    cursor.execute(sql, (amount, account_id))
    cursor.execute('COMMIT;')
