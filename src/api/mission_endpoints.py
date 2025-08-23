from flask import Blueprint, jsonify, request
from src.missions.mission_registry import MissionRegistry

mission_api = Blueprint('mission_api', __name__)

@mission_api.route('/missions', methods=['GET'])
def get_missions():
    missions = MissionRegistry.get_all_missions()
    return jsonify(missions), 200

@mission_api.route('/missions/<string:mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = MissionRegistry.get_mission(mission_id)
    if mission:
        return jsonify(mission), 200
    return jsonify({'error': 'Mission not found'}), 404

@mission_api.route('/missions/<string:mission_id>/submit', methods=['POST'])
def submit_mission(mission_id):
    data = request.json
    user_code = data.get('code')
    # Here you would add logic to validate the user's code
    # For now, we will just return a success message
    return jsonify({'message': 'Mission submitted successfully', 'mission_id': mission_id}), 201