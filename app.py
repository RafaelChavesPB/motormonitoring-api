from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods = ['GET'])
def get_index():
    return 'Hello World'

if __name__ == '__main__':
    socketio.run(app)