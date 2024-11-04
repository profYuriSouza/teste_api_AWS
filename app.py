from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas em memória
tarefas = [
    {'id': 1, 'titulo': 'Comprar leite', 'descricao': 'Comprar 2 litros de leite', 'feito': False},
    {'id': 2, 'titulo': 'Estudar Python', 'descricao': 'Ler sobre Flask', 'feito': False}
]

# Obter todas as tarefas
@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify({'tarefas': tarefas})

# Obter uma tarefa pelo ID
@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def obter_tarefa(tarefa_id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == tarefa_id), None)
    return jsonify({'tarefa': tarefa}) if tarefa else ('', 404)

# Criar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = {
        'id': tarefas[-1]['id'] + 1 if tarefas else 1,
        'titulo': request.json['titulo'],
        'descricao': request.json.get('descricao', ''),
        'feito': False
    }
    tarefas.append(nova_tarefa)
    return jsonify({'tarefa': nova_tarefa}), 201

# Atualizar uma tarefa existente
@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == tarefa_id), None)
    if tarefa:
        tarefa['titulo'] = request.json.get('titulo', tarefa['titulo'])
        tarefa['descricao'] = request.json.get('descricao', tarefa['descricao'])
        tarefa['feito'] = request.json.get('feito', tarefa['feito'])
        return jsonify({'tarefa': tarefa})
    else:
        return ('', 404)

# Deletar uma tarefa
@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
