from flask import Blueprint, jsonify, request, make_response
from flask.ext.httpauth import HTTPBasicAuth
import time, datetime


""" Create an API Blueprint: """
apis = Blueprint('api', __name__)


""" Init Auth layer: """
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None


""" Return 403 instead of 401 to prevent browsers from displaying the default auth dialog """
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@apis.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@apis.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



""" Add default task: """
tasks_list = [
    {
        'id': 1,
        'title': u'New Task',
        'description': u'Create a new task using the REST APIs',
        'created': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
        'done': 1
    },
]


""" Welcome message: """
@apis.route('/')
def welcome():
        return jsonify(["Welcome - Flask API examples"])


""" Get list of tasks: """
@apis.route('/tasks', methods=['GET'])
@auth.login_required
def list_tasks():
    return jsonify(tasks_list)


""" Flush tasks: """
@apis.route('/tasks', methods=['DELETE'])
@auth.login_required
def delete_tasks():
    global tasks_list
    tasks_list = []
    return jsonify(tasks_list)


"""
Add a new task:
Title, Description and Done flag must be passed as HTTP Header parameters.
"""
@apis.route('/tasks', methods=['POST'])
@auth.login_required
def add_tasks():
    if 'title' in request.headers and isinstance(request.headers['title'], basestring):
        title=request.headers['title']
    else :
        return make_response(jsonify({'error': 'Missing title'}), 400)

    if 'description' in request.headers and isinstance(request.headers['description'], basestring):
        description=request.headers['description']
    else:
        return make_response(jsonify({'error': 'Missing description'}), 400)

    if 'done' in request.headers and int(request.headers['done']) in range(0, 2):
        done=request.headers['done']
    else:
        return make_response(jsonify({'error': 'Missing done'}), 400)
    task={
        'id': len(tasks_list) + 1,
        'title': title,
        'description': description,
        'created': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
        'done': done
    }
    tasks_list.append(task)
    return jsonify(tasks_list)


""" Get a task by ID: """
@apis.route('/task/<int:id>', methods=['GET'])
@auth.login_required
def task(id):
    id -= 1
    if id in range(0, len(tasks_list)):
        return jsonify(tasks_list[id])
    else:
        return make_response(jsonify({'error': 'Task id %d not found' % id}), 400)


""" Delete a task by ID: """
@apis.route('/task/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_task(id):
    if id in range(1, len(tasks_list) + 1):
        del tasks_list[id]
        return jsonify(tasks_list)
    else:
        return make_response(jsonify({'error': 'Task id %d not found' % id}), 400)


""" Update a task by ID: """
@apis.route('/task/<int:id>', methods=['POST'])
@auth.login_required
def udpate_task(id):
    if id in range(1, len(tasks_list) + 1):

        global tasks_list
        id = next(index for (index, d) in enumerate(tasks_list) if d["id"] == id)

        if 'title' in request.headers and isinstance(request.headers['title'], basestring):
            tasks_list[id]['title'] = request.headers['title']

        if 'description' in request.headers and isinstance(request.headers['description'], basestring):
            tasks_list[id]['description'] = request.headers['description']

        if 'done' in request.headers and int(request.headers['done']) in range(0, 2):
            tasks_list[id]['done'] = int(request.headers['done'])

        return jsonify(tasks_list[id])
    else:
        return make_response(jsonify({'error': 'Task id %d not found' % id}), 400)