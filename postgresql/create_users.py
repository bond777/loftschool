from postgresql.connection import connection
from datetime import datetime

with connection.cursor() as cursor:
    sql = """
        insert into "user" 
            (name, phone, created_at) 
        VALUES
            ('Гарри Поттер', '79990000000', %s),
            ('Гермиона Грейнджер', '79990000001', %s),
            ('Волан-де-Морт', '79990000002', %s),
            ('Альбус Дамблдор', '79990000003', %s),
            ('Северус Снегг', '79990000004', %s),
            ('Драко Малфой', '79990000005', %s),
            ('Сириус Блэк', '79990000006', %s)
    """
    cursor.execute(sql, [datetime.now(), datetime.now(), datetime.now(),
        datetime.now(), datetime.now(), datetime.now(), datetime.now()])
connection.commit()
