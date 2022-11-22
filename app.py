from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    join_room(data['room'])
    emit('chat message', data['msg'], to=data['room'])
