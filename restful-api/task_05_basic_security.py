#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ------------------------
# BASIC AUTHENTICATION
# ------------------------
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ------------------------
# JWT LOGIN
# ------------------------
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": token})


# ------------------------
# JWT PROTECTED ROUTE
# ------------------------
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ------------------------
# ADMIN-ONLY ROUTE
# ------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# ------------------------
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# ------------------------
@jwt.unauthorized_loader
def jwt_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def jwt_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def jwt_expired_token(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def jwt_needs_fresh_token(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def jwt_revoked_token(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401


if __name__ == "__main__":
    app.run()
