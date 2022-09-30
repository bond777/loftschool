from postgresql.connection import connection


with connection.cursor() as cursor:
    sql = """
        CREATE TABLE account(
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name VARCHAR(32) NOT NULL,
            balance NUMERIC(10,2) NOT NULL,
            CONSTRAINT fk_user
                FOREIGN KEY(user_id) REFERENCES "user" (id)
        );
    """
    cursor.execute(sql)
