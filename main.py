from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = '70cabb17ba12180ef937000d1adc8782'
socketio = SocketIO(app, cors_allowed_origins=["http://127.0.0.1:5000", "http://localhost:5000"])

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Your logic to handle the message goes here.
    return jsonify({"status": "success", "message": "Message received"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
