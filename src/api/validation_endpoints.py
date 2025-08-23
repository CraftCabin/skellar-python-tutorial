from flask import Blueprint, request, jsonify
from validators.python_runner import PythonRunner

validation_bp = Blueprint('validation', __name__)

@validation_bp.route('/validate', methods=['POST'])
def validate_code():
    data = request.json
    code = data.get('code')
    expected_output = data.get('expected_output')

    if not code or expected_output is None:
        return jsonify({'error': 'Code and expected_output are required'}), 400

    runner = PythonRunner()
    result = runner.run(code)

    if result['error']:
        return jsonify({'error': result['error']}), 400

    is_correct = result['output'] == expected_output
    return jsonify({'is_correct': is_correct, 'output': result['output']})