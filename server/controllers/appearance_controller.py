from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from config import db
from flask_jwt_extended import jwt_required

appearances_bp = Blueprint('appearances_bp', __name__)

@appearances_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except Exception:
        return jsonify({'errors': ['Validation errors']}), 400
