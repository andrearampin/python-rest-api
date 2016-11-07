# Flask REST APIs example - Task List
This is an example of how to use Flask to create a list of tasks using RESTFUL APIs and Basic Authentication.

## Set up virtual environment
Once the repository has been cloned, run the following command to start the virtual environment, install all the required libraried and run the server.

```
$ chmod +x setup.sh && ./setup.sh
```

## Endpoints

### /
Publicly accessible.

```$ curl http://127.0.0.1:5000```

### /tasks (GET)
Display the list of tasks.

```$ curl --user admin:admin http://127.0.0.1:5000/tasks```

### /tasks (DELETE)
Delete all the stored tasks.

```$ curl -X "DELETE" --user admin:admin http://127.0.0.1:5000/tasks```

### /tasks (POST)
Add a new task.

```$ curl -X "POST" --user admin:admin -H "title:title" -H "description:description" -H "done:0"  http://127.0.0.1:5000/tasks```

### /task/<int:id> (GET)
Display a task give the ID.

```$ curl --user admin:admin http://127.0.0.1:5000/task/1```

### /task/<int:id> (DELETE)
Delete a task given the ID.

```$ curl -X "DELETE" --user admin:admin http://127.0.0.1:5000/task/1```

### /task/<int:id> (POST)
Update a task given the ID.

```$ curl -X "POST" --user admin:admin -H "done:1"  http://127.0.0.1:5000/task/1```