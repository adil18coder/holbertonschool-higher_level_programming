#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty users dictionary (DO NOT add test users here)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    # Return list of all usernames
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    # Check if body is valid JSON
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check username existence
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
