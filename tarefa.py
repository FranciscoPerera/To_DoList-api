from flask import jsonify
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

def buscar_tarefa():
    # Conecta no banco 
    conect = get_conexao()
    cursor = conect.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s", (id,)
    )

    # Busca o s dados e armazena na variavel
    todo = cursor.fetchone()

    # Fecha as conexoes
    cursor.close()
    conect.close()

    return jsonify(todo)