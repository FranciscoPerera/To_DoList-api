from flask import jsonify
from psycopg2 import connect
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    # Conecta no banco 
    conect = get_conexao()
    cursor = conect.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos"
    )

    # Busca o s dados e armazena na variavel
    todos = cursor.fetchall()

    # Fecha as conexoes
    cursor.close()
    conect.close()

    return jsonify(todos)

def buscar_tarefa(id):
    # Conecta no banco 
    conect = get_conexao()
    cursor = conect.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s", (id,)
    )

    # Busca os dados e armazena na variavel
    todo = cursor.fetchone()

    # Fecha as conexoes
    cursor.close()
    conect.close()

    return jsonify(todo)

def criar_tarefa(name, description):
    # Conecta no banco 
    conect = get_conexao()
    cursor = conect.cursor()
    cursor.execute(
        "INSERT INTO todos (name, description) VALUES (%s, %s)",
        (name, description)
    )

    # Envia as modificações para o banco de dados
    conect.commit()

    # Encerra as conexoes com o banco de dados
    cursor.close()
    conect.close()