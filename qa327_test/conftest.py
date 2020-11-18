import pytest
import subprocess
import os
import signal
import time
import tempfile
from qa327.__main__ import FLASK_PORT
from qa327.__main__ import app
from qa327.models import db
import threading
from werkzeug.serving import make_server


base_url = 'http://localhost:{}'.format(FLASK_PORT)

class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', FLASK_PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()
        with self.ctx:
            db.drop_all()
            db.create_all()
            db.session.commit()

    def shutdown(self):
        self.srv.shutdown()


@pytest.fixture(scope="module", autouse=True)
def server():

    on_win = os.name == 'nt'
    # create a live server for testing
    # with a temporary file as database
    server = ServerThread()
    server.start()
    time.sleep(1)
    yield
    server.shutdown()
    time.sleep(1)
