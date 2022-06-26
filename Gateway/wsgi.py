from app import app
from app import socketio

if __name__ == "__main__":
    #socketio.run(app, host='127.0.0.1', port=5000, certfile='cert.pem', keyfile='key.pem')
    socketio.run(app, host='127.0.0.1', port=5000)
    #app.run(host='127.0.0.1', port=5000, ssl_context=('cert.pem','key.pem'))