from postgresql.connection import connection
from datetime import datetime

with connection.cursor() as cursor:
    sql = """
        insert into "user" 
            (name, phone, created_at) 
        VALUES
            ('Распус Люпин', '79990000000', %s)
    """
    cursor.execute(sql, [datetime.now()])

