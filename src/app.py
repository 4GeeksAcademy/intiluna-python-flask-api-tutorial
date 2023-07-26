from flask import Flask,jsonify,request
app = Flask(__name__)


# suppose you have your data in the variable named some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

# todos variable
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoints
@app.route('/myroute', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # and then you can return it to the front end in the response body like this
    return json_text



@app.route('/todos', methods=['GET'])
def hello():
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text


# add post endpoint
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text

# add delete endpoint
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)