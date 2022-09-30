from postgresql.connection import connection


with connection.cursor() as cursor:
    sql = """
        CREATE TABLE "user" (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) NOT NULL, 
            phone VARCHAR(11) NOT NULL UNIQUE,
            created_at timestamp NOT NULL
        );
    """
    cursor.execute(sql)
