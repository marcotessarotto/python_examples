# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from flask_app.user_input_collector import UserInputCollector

app = Flask(__name__)
socketio = SocketIO(app)

collector = UserInputCollector()

@app.route('/')
def index():
    return render_template('index.html')

# @socketio.on('send_input')
# def handle_input(message):
#     # Here, you'd send the message to your Python script and get the output
#     # For demonstration, I'm just echoing the message back
#     output = f"Received: {message['data']}"
#     emit('script_output', {'data': output})


@socketio.on('send_input')
def handle_input(message):
    collector.add_input(message['data'])
    if collector.is_complete():
        emit('script_output', {'data': f"Total number of characters: {collector.get_total_characters()}"})
    else:
        emit('request_input', {'data': f"Enter input {collector.count + 1}:"})


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)

# Path: flask_app/templates/index.html
