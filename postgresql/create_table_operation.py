from postgresql.connection import connection


with connection.cursor() as cursor:
    sql = """
        CREATE TABLE operation(
            id SERIAL PRIMARY KEY,
            amount NUMERIC(10,2) NOT NULL,
            account_id INTEGER NOT NULL, 
            created_at timestamp NOT NULL,
            CONSTRAINT fk_account
                FOREIGN KEY(account_id) REFERENCES "account" (id)
        );
    """
    cursor.execute(sql)

