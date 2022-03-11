import os
import time

from app import app

if __name__ == "__main__":
    os.system('flask db init')
    os.system('flask db stamp head')
    os.system('flask db migrate')
    os.system('flask db upgrade')
    time.sleep(3)
    app.run()
