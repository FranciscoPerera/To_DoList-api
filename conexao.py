import psycopg2

def get_conexao():
    conn = psycopg2.connect(
        dbname = 'todo_list',
        user = 'postgres',
        password = 'postgres',
        host = '127.0.0.1',
        port = 5432
    )
    return conn