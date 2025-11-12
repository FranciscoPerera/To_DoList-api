from flask import Flask, request
from tarefa import buscar_tarefas
from tarefa import buscar_tarefa
from tarefa import criar_tarefa
from tarefa import apagar_tarefa
from tarefa import atualizar_tarefa

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return{
        'message': 'Api Rodando!'
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

@app.route('/api/tarefa/<int:todo_id>', methods=['GET'])
def get_tarefa(todo_id):
    tarefa = buscar_tarefa(todo_id)
    return tarefa

@app.route('/api/tarefas', methods=['POST'])
def create_tarefa():
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_description =corpo.get('description')
    criar_tarefa(tarefa_name, tarefa_description)

    return{
        'message': 'Tarefa Cadastrada Com Sucesso'
    }

@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    apagar_tarefa(tarefa_id)

    return{
        'message': 'Tarefa Deletada Com Sucesso'
    }

@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def update_tarefa(tarefa_id):
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_description =corpo.get('description')
    atualizar_tarefa(tarefa_id, tarefa_name, tarefa_description)

    return{
        'message': 'Tarefa Atualizada Com Sucesso'
    }

# Se for o modulo principal roda o projeto em debug
if __name__ == '__main__':
    app.run(debug=True)