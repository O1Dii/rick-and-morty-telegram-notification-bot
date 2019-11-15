from flask import jsonify, request

from app import app
from app.telegram_commands import handle_command, handle_ordinary_message


@app.route('/', methods=['POST', 'GET'])
def index():
    message = request.get_json().get('message')

    if not message:
        return jsonify('')

    if message['text'][0] == '/':
        handle_command(message)
    else:
        handle_ordinary_message(message)

    return jsonify('')
