from app import app, db
from flask import jsonify, request
from models import TodoList
from serializer import todoSchemas, todoSchema

# routes
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()

    todo = TodoList(**data)
    db.session.add(todo)
    db.session.commit()
    result = todoSchema.dump(todo)
    return jsonify(result)

@app.route("/todos", methods=['GET'])
def read_todo():
    data = TodoList.query.all()
    result = todoSchemas.dump(data)
    return jsonify(result)

@app.route("/todos/<int:id>")
def get_a_todo(id):
    todo = TodoList.query.filter_by(id=int(id)).first()
    result = todoSchema.dump(todo)
    return jsonify(result)

@app.route("/todos/<int:id>", methods=['PUT'])
def update_todo(id):
    todo = TodoList.query.filter_by(id=int(id)).first()
    title = request.get_json()['title']
    description = request.get_json()['description']
    todo.title = title
    todo.description = description
    db.session.commit()
    result = todoSchema.dump(todo)
    return jsonify(result)

@app.route("/todos/<int:id>", methods=['DELETE'])
def delete_todo(id):
    todo = TodoList.query.get(int(id))
    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"})
