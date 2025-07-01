from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE = "users.json"

def read_users():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def write_users(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/users", methods=["POST"])
def create_user():
    user = request.get_json()
    users = read_users()
    users.append(user)
    write_users(users)
    return {"message": "User added"}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(read_users())

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = read_users()
    users = [u for u in users if u.get("id") != user_id]
    write_users(users)
    return {"message": "User deleted"}

@app.route("/users/<email>", methods=["PUT"])
def update_user(email):
    data = request.get_json()
    users = read_users()
    for user in users:
        if user.get("email") == email:
            user.update(data)
            write_users(users)
            return {"message": "User updated"}
    return {"message": "User not found"}, 404

@app.route("/", methods=["GET"])
def home():
    return {"message": "Welcome! Use /users to manage user data."}

if __name__ == "__main__":
    app.run()
