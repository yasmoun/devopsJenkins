from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Liste de tâches initiale
tasks = [
    {
        'id': 1,
        'title': 'Acheter du lait',
        'description': 'Acheter du lait au supermarché',
        'done': False
    },
    {
        'id': 2,
        'title': 'Apprendre Flask',
        'description': 'Lire la documentation de Flask et créer une API',
        'done': False
    }
]

# Route pour obtenir toutes les tâches
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route pour obtenir une tâche par ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify({'task': task})

# Route pour créer une nouvelle tâche
@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Route pour mettre à jour une tâche existante
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# Route pour supprimer une tâche
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    tasks.remove(task)
    return jsonify({'result': True})

# Route pour la page d'accueil
@app.route('/')
def index():
    return "Bienvenue à l'API de gestion des tâches!"

if __name__ == '__main__':
    app.run(debug=True)