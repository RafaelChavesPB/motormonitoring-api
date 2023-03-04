from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods = ['GET'])
def get_index():
    return 'Olá este é o backend da aplicação motormonitoring'

@app.route('/', methods = ['POST'])
def get_post():
    socketio.emit('incoming_data', {'message': 'hello world'})
    return 'sad'

if __name__ == '__main__':
    socketio.run(app)