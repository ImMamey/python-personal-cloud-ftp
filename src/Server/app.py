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
import os
import logging
import platform
import sqlite3
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from src.Server.utils import setup_logger, user_dir, get_ip
from environment import env
from src.Server.adminpanel import Ui_MainWindow

LOG = logging.getLogger("server")


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.username = ""
        self.password = ""


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
        if self.lineEditPassword.text() == "" and self.lineEditUser.text() == "":
            self.checkinputlabel.setText("Credentials cant be empty")
            self.lineEditUser.setText("")
            self.lineEditPassword.setText("")
            return False

        elif self.lineEditPassword.text() == "":
            self.checkinputlabel.setText("Please enter a valid password")
            self.lineEditUser.setText("")
            self.lineEditPassword.setText("")
            return False

        elif self.lineEditUser.text() == "":
            self.checkinputlabel.setText("Please enter a valid username")
            self.lineEditUser.setText("")
            self.lineEditPassword.setText("")
            return False
        elif self.lineEditPassword.text() != "" and self.lineEditUser.text() != "":
            return True

    def create_clicked(self) -> None:

        if self.lineEdite_validation():
            username = self.lineEditUser.text()
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

    def sql_admin_login(self) -> None:
        """
        Logs in with an existing admin account if possible
        :return:None
        """
        # Saves current data from the Usernames
        if self.lineEdite_validation():
            self.username = self.lineEditUser.text()
            self.password = self.lineEditPassword.text()
            db = None
            try:
                db = sqlite3.connect("users.db")
            except Exception as e:
                print(e)

            # SQL commands and cursors
            command_login = f'''SELECT username FROM admins where username = "{self.username}" and password = "{self.password}";'''
            cursor = db.cursor()

            # Check for admin match
            cursor.execute(command_login)
            if not cursor.fetchone():
                msg = QMessageBox()
                msg.setWindowTitle("Failiure!")
                msg.setText(f"Admin credentials are wrong, please try again")
                msg.setStandardButtons(QMessageBox.Retry)
                x = msg.exec_()
            else:
                print("Logged in!")
                self.openWindow()

            db.commit()
            db.close()

    def sql_create_admin(self) -> None:
        """
        Create a db connection, and creates and admin if possible
        :return: None
        """
        # connection with DB
        db = None
        try:
            db = sqlite3.connect("users.db")
        except Exception as e:
            print(e)

        # SQL commands and cursors
        command_check = f'SELECT COUNT(*) FROM admins'
        command_insert = f'INSERT INTO admins(username, password) values(? , ?)'
        command_chkrepeatedadmin = f'SELECT username FROM admins where username = ?;'
        cursor = db.cursor()

        # CHECKS IF there are more than 2 ADMINS
        cursor.execute(command_check)
        value = cursor.fetchone()

        if value[0] == 2:
            msg = QMessageBox()
            msg.setWindowTitle("You cant create more admins")
            msg.setText(f"You only can have 2 admins accounts with this program.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        elif value[0] < 2:
            cursor.execute(command_chkrepeatedadmin, (self.username,))
            if not cursor.fetchone():
                print("Repeated admin")
            else:
                print("Created 1 admin")
                cursor.execute(command_insert, (self.username, self.password))
                # src.Server.ftpserver.start()
        db.commit()
        db.close()


    def ok_button_clicked(self, i):
        if i.text() == "OK":
            self.sql_create_admin()
        if i.text() == "Retry":
            self.username = ""
            self.password = ""

    def onClick(self):
        print('start')
        server_ip = get_ip()
        user = self.lineEditUser.text()
        passw = self.lineEditPassword.text()

        self.authorizer.add_user(user, passw, '.', perm='elrw')
        self.address = ('127.0.0.1', 2100)
        self.server = ThreadedFTPServer(self.address, self.handler)

        QMessageBox.information(self, "FTP Server started", "FTP Server started")
        self.start()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.refreshed_button_pressed()
        win.close()

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
