

from flask import Flask,request

app = Flask(__name__)

tarefas = [
    {
        "id":1,
        "titulo": "Estudar Java",
        "descricao":"Estudar Java para aprender construir tarefas ",
        "status":"Em andamento ",
        "data": "29/03/25",
        "materia": "dev",
        "finalizacao": "05/04/25"
    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre Web services ",
        "status": "Nao iniciado ",
        "data": "09/01/25",
        "materia": "dev",
        "finalizacao": "10/04/25"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id')== task_id:
            return tarefa
    return 'Tarefa nao encontrada '

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id']= ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['data'] = task_body.get('data')
    task_search['materia'] = task_body.get('materia')
    task_search['finalizacao'] = task_body.get('finalizacao')


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return {'message': "A tarefa foi deletada"}

    return {'message':"Não foi possível encontrar a tarefa"}

if __name__ == '__main__':
    app.run(debug=True)