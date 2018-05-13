import socketio
import eventlet
from flask import Flask, render_template

# import logging
# log = logging.getLogger('werkzeug')
# logging.basicConfig(filename='logs/app.log', level=logging.INFO)
# log.setLevel(logging.ERROR)
# print(log)

sio = socketio.Server()
app = Flask(__name__, static_folder='static', template_folder='template', static_url_path='')

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

# @sio.on('loaded_ack')
@app.route('/<data>', methods=['GET'])
def message(data):
    print('Loaded: ', data)
    if data:
        sio.emit("data", data)
    return "Data Sent"

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)