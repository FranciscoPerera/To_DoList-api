from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitação',
            'descricao': 'Vamos aumentar o zoom para nao errar',
            'status': 'Pendente'
        },
        {
            'id': 2,
            'nome': 'Aprender Python',
            'descricao': 'Aprender Python para programar Api',
            'status': 'Concluida'
        },
        {
            'id': 3,
            'nome': 'Aprender a biblioteca Flask',
            'descricao': 'Aprender Flask para programar',
            'status': 'Pendente'
        }
    ]

    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
        'id': 1,
        'nome': 'Aprender digitação',
        'descricao': 'Vamos aumentar o zoom para nao errar',
        'status': 'Pendente'
    },
        
    return jsonify(tarefa)