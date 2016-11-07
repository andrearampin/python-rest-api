# Flask REST APIs example - Task List
This is an example of how to use Flask to create a list of tasks using RESTFUL APIs and Basic Authentication.

## Set up virtual environment
Once the repository has been cloned, run the following command to start the virtual environment, install all the required libraried and run the server.

```
$ chmod +x setup.sh && ./setup.sh
```

## Endpoints

### @apis.route('/')
Publicly accessible.

```$ curl http://127.0.0.1:5000```

### @apis.route('/tasks', methods=['GET'])
Display the list of tasks.

```$ curl --user admin:admin http://127.0.0.1:5000/tasks```

### @apis.route('/tasks', methods=['DELETE'])
Delete all the stored tasks.

```$ curl -X "DELETE" --user admin:admin http://127.0.0.1:5000/tasks```

### @apis.route('/tasks', methods=['POST'])
Add a new task.
```$ curl -X "POST" --user admin:admin -H "title:title" -H "description:description" -H "done:0"  http://127.0.0.1:5000/tasks```

### @apis.route('/task/<int:id>', methods=['GET'])
Display a task give the ID.

```$ curl --user admin:admin http://127.0.0.1:5000/task/1```

### @apis.route('/task/<int:id>', methods=['DELETE'])
Delete a task given the ID.

```$ curl -X "DELETE" --user admin:admin http://127.0.0.1:5000/task/1```

### @apis.route('/task/<int:id>', methods=['POST'])
Update a task given the ID.

```$ curl -X "POST" --user admin:admin -H "done:1"  http://127.0.0.1:5000/task/1```