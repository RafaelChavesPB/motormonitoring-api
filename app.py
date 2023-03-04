from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/', methods=['GET'])
def get_index():
    return 'Olá este é o backend da aplicação motormonitoring'


@app.route('/', methods=['POST'])
def get_post():
    current = int(request.form.get('current', 0))
    voltage = int(request.form.get('voltage', 0))
    time = datetime.now().strftime("%H:%M:%S")
    data = {'current': current, 'voltage': voltage, 'time': time}
    socketio.emit('incoming_data', data)
    return '200'


if __name__ == '__main__':
    socketio.run(app, debug=True)
