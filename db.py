import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="employee_db",
        user="postgres",
        password="Fbisd712176!!",
        port="5432"
    )
