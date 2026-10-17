from flask import Flask, request, abort, json, jsonify

app=Flask(__name__)


#1-obtener tareas
@app.route("/task")
def get_task():
    status=request.args.get("status")
    with open ('task.json', 'r') as f:
        tasks=json.load(f)
    if status:
        tasks=[task for task in tasks if task['status']==status]
            
    return jsonify(tasks)


#2- crear tareas.
@app.route("/task", methods=['POST'])
def make_task():
    request_body=request.json
    with open('task.json', 'r') as f:
        tasks=json.load(f)
        try:
            for task in tasks:
                if task['id']==request_body['id']:
                    raise ValueError("The ID already exists.")
                if not request_body.get('title') or not request_body.get('description') or not request_body.get('status'):
                    raise ValueError('Please provide all required fields.')
                if request_body.get('status') not in ['to do', 'in progress', 'completed']:
                    raise ValueError('The status is invalid; choose from to do, in progress, or completed.')
        
            tasks.append(request_body)
            with open('task.json', 'w') as f:
                json.dump(tasks, f)
            return jsonify(tasks)
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500
        

#3-editar tareas
@app.route("/task", methods=['PATCH'])
def update_task():
    request_body=request.json
    with open ('task.json', 'r') as f:
        tasks=json.load(f)
        try:
            if 'status' in request_body:
                if request_body.get('status') not in ['to do', 'in progress', 'completed']:
                    raise ValueError('The status is invalid; choose from to do, in progress, or completed.')
            found_task=False
            for task in tasks:
                if task["id"]==request_body["id"]:
                    found_task=True
                    task.update(request_body)
            if not found_task:
                raise ValueError('task not found')
            with open('task.json', 'w') as f:
                json.dump(tasks, f)
            return jsonify(tasks)
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500



#4-eliminar tareas
@app.route("/task",methods=['DELETE'])
def delete_task():
    request_body=request.json
    with open('task.json', 'r') as f:
        tasks=json.load(f)
        try:
            found_task= False
            for task in tasks:
                if request_body.get('id')==task['id']:
                    found_task=True
            if not found_task:
                raise ValueError('task not found')
            tasks=[task for task in tasks if task['id']!=request_body['id']]
            with open('task.json', 'w') as f:
                json.dump(tasks, f)
            return jsonify(tasks)
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500




if __name__ =="__main__":
    app.run(host="localhost", port=7000, debug=True)