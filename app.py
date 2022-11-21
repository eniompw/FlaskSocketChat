from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('chat message')
def send_msg(data):
    emit('chat message', data, broadcast=True)
