import psycopg2

connection = psycopg2.connect(
    database='loft_school_bank',
    host='localhost',
    user='admin',
    password='!AS6DF:LD3LKJdsfh'
)
connection.autocommit = True
