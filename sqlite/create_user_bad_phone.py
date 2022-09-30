import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        insert into user 
            (name, phone, created_at) 
        VALUES
            ('Распус Люпин', '+79990000000', '2022-09-14T08:19:52.672702')
    """
    cursor.execute(sql)
