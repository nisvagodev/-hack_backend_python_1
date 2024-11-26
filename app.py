from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#1
@app.route("/users", methods=["GET"])
def users():
    return jsonify({'payload':'success'})

#2
@app.route("/user", methods=["POST"])
def user():
    return jsonify({'payload':'success'})

#3
@app.route("/user", methods=["DELETE"])
def user_delete():
    return jsonify({'payload':'success'})

#4
@app.route("/user", methods=["PUT"])
def user_put():
    return jsonify({'payload':'success', 'error': False})

#5 
@app.route("/api/v1/users", methods=["GET"])
def v1_users():
    return jsonify({'payload':[]})

#6
@app.route("/api/v1/user", methods=["POST"])
def v1_user():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
        }
    })
    
#7
@app.route("/api/v1/user/add", methods=["POST"])
def v1_user_add():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    })

#8
@app.route("/api/v1/user/create", methods=["POST"])
def v1_user_create():
    request_data = request.get_json()
    email = request_data['email']
    name = request_data['name']
    id = request_data['id']
    return jsonify({
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    })



if __name__ == "__main__":
    app.run(debug=True)