from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    return render_template('send.html')

@socketio.on('send')
def send_msg(data):
    emit('response', data, broadcast=True)

# https://pythonprogramminglanguage.com/python-flask-websocket
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html#broadcasting
# https://www.sitepoint.com/get-url-parameters-with-javascript
