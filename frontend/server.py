import socketio
import eventlet
from flask import Flask, render_template

ANS='00000'
PREV_ANS=ANS
PRESSED = False

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

@sio.on('msg_backend')
def msg_backend(sid, data):
    print('BACKEND: ', data)
    sio.emit("data", data)

if __name__ == '__main__':
    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)