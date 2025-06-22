from flask import Blueprint, jsonify, request
from models.episode import Episode
from config import db
from flask_jwt_extended import jwt_required

episodes_bp = Blueprint('episodes_bp', __name__)

@episodes_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date, 'number': e.number} for e in episodes])

@episodes_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict())

@episodes_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({}), 204
