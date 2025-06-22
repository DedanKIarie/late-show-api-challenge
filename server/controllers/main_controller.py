from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Late Show API!",
        "api_routes": [
            "/register",
            "/login",
            "/episodes",
            "/guests",
            "/appearances"
        ]
    })
