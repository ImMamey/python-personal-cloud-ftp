# FTP server gui with PyQt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import sys
import os
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from src.Server.utils import setup_logger, user_dir, get_ip
from environment import env

LOG = logging.getLogger("server")


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)

        #actions and events
        self.pushButtonStart.clicked.connect(self.onClick)
        self.pushButtonStop.clicked.connect(self.onStop)
        self.pushButtonCreate.clicked.connect(self.create_clicked)
        self.pushButtonLogin.clicked.connect(self.sql_admin_login)

        self.authorizer = DummyAuthorizer()
        self.authorizer.add_anonymous(os.getcwd())

        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer
        self.handler.banner = "pyftpdlib based ftpd ready."

        # set a limit for connections
        self.max_cons = 256
        self.max_cons_per_ip = 5
    def lineEdite_validation(self) -> bool:
        if self.lineEditPassword.text() == "" and self.lineEditUsername.text() == "":
            self.checkinputlabel.setText("Credentials cant be empty")
            self.lineEditUsername.setText("")
            self.lineEditPassword.setText("")
            return False

        elif self.lineEditPassword.text() == "":
            self.checkinputlabel.setText("Please enter a valid password")
            self.lineEditUsername.setText("")
            self.lineEditPassword.setText("")
            return False

        elif self.lineEditUsername.text() == "":
            self.checkinputlabel.setText("Please enter a valid username")
            self.lineEditUsername.setText("")
            self.lineEditPassword.setText("")
            return False
        elif self.lineEditPassword.text() != "" and self.lineEditUsername.text() != "":
            return True
    def create_clicked(self) -> None:

        if self.lineEdite_validation():
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()

            msg = QMessageBox()
            msg.setWindowTitle("Attention, please save your credentials somewhere safe!")
            msg.setText(f"Please, save your credentials somewhere safe, and then click on OK\n\n"
                        f"Your current Username is: {username}\n"
                        f"Your current Password is: {password}\n\n"
                        f"If you want to use different credentials, please click on Retry")
            self.username = username
            self.password = password

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Retry)

            msg.buttonClicked.connect(self.ok_button_clicked)
            x = msg.exec_()

    def onClick(self):
        print('start')

        user = self.lineEditUser.text()
        passw = self.lineEditPassword.text()

        self.authorizer.add_user(user, passw, '.', perm='elrw')
        self.address = ('127.0.0.1', 2100)
        self.server = ThreadedFTPServer(self.address, self.handler)

        QMessageBox.information(self, "FTP Server started", "FTP Server started")
        self.start()

    def _run_server(self):
        self.server.serve_forever()

    def start(self):
        srv = threading.Thread(target=self._run_server)
        srv.deamon = True
        srv.start()

    def onStop(self):
        print('stop')
        self.server.close_all()
        QMessageBox.information(self, "FTP Server stopped", "FTP Server stopped")


app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
