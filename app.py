from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('recieve.html')

@app.route('/outbox')
def outbox():
    return render_template('outbox.html')

@app.route('/send')
def send():
    return render_template('send.html')

@socketio.on('connect')
def default(auth):
    emit('response', 'Welcome')

@socketio.on('send')
def send_msg(data):
    emit('response', data, broadcast=True)

# https://pythonprogramminglanguage.com/python-flask-websocket
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html#broadcasting
# https://www.sitepoint.com/get-url-parameters-with-javascript
