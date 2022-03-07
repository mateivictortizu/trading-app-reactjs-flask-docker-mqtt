from app import app
import os
import time

if __name__ == "__main__":
    #os.system('flask db stamp head')
    #os.system('flask db migrate')
    #os.system('flask db upgrade')
    #time.sleep(3)
    app.run(host='127.0.0.1', port=5001, debug=True, ssl_context=('cert.pem', 'key.pem'))
