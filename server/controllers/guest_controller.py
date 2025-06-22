from flask import Blueprint, jsonify
from models.guest import Guest

guests_bp = Blueprint('guests_bp', __name__)

@guests_bp.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])
