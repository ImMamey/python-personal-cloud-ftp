# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminpanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import ip


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #global class variables
        self.create_username = ""
        self.create_password = ""
        self.create_almacenamiento = 0


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 761, 451))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setToolTipDuration(0)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_users = QtWidgets.QTableWidget(self.tab)
        self.table_users.setGeometry(QtCore.QRect(40, 61, 661, 361))
        self.table_users.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_users.setAutoFillBackground(False)
        self.table_users.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.table_users.setFrameShape(QtWidgets.QFrame.Box)
        self.table_users.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_users.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_users.setObjectName("table_users")
        self.table_users.setColumnCount(3)
        self.table_users.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, item)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(450, 9, 238, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.lineEdit_searchUser_view = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_searchUser_view.setObjectName("lineEdit_searchUser_view")
        self.horizontalLayout_8.addWidget(self.lineEdit_searchUser_view)
        self.pushButton_searchUser_view = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_searchUser_view.setObjectName("pushButton_searchUser_view")
        self.horizontalLayout_8.addWidget(self.pushButton_searchUser_view)
        self.pushButton_Refresh_view = QtWidgets.QPushButton(self.tab)
        self.pushButton_Refresh_view.setGeometry(QtCore.QRect(40, 20, 75, 23))
        self.pushButton_Refresh_view.setObjectName("pushButton_Refresh_view")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(159, 90, 391, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_createUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_createUsername.setObjectName("lineEdit_createUsername")
        self.horizontalLayout.addWidget(self.lineEdit_createUsername)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_createPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_createPassword.setObjectName("lineEdit_createPassword")
        self.horizontalLayout_2.addWidget(self.lineEdit_createPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_storage_createUser = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_storage_createUser.setObjectName("spinBox_storage_createUser")
        self.horizontalLayout_3.addWidget(self.spinBox_storage_createUser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.button_create_user = QtWidgets.QPushButton(self.tab_2)
        self.button_create_user.setGeometry(QtCore.QRect(268, 370, 201, 23))
        self.button_create_user.setObjectName("button_create_user")
        self.info_label_create = QtWidgets.QLabel(self.tab_2)
        self.info_label_create.setGeometry(QtCore.QRect(20, 40, 691, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_label_create.setFont(font)
        self.info_label_create.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                             "color: rgb(255, 0, 0);")
        self.info_label_create.setText("")
        self.info_label_create.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label_create.setObjectName("info_label_create")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(170, 60, 171, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_editUser = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_editUser.setGeometry(QtCore.QRect(320, 60, 181, 20))
        self.lineEdit_editUser.setObjectName("lineEdit_editUser")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 120, 391, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_editUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_editUsername.setObjectName("lineEdit_editUsername")
        self.horizontalLayout_4.addWidget(self.lineEdit_editUsername)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_editPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_editPassword.setObjectName("lineEdit_editPassword")
        self.horizontalLayout_5.addWidget(self.lineEdit_editPassword)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.spinBox_editStorage = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_editStorage.setObjectName("spinBox_editStorage")
        self.horizontalLayout_6.addWidget(self.spinBox_editStorage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton_editUser = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_editUser.setGeometry(QtCore.QRect(280, 400, 211, 23))
        self.pushButton_editUser.setObjectName("pushButton_editUser")
        self.info_label_edit = QtWidgets.QLabel(self.tab_4)
        self.info_label_edit.setGeometry(QtCore.QRect(30, 90, 691, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_label_edit.setFont(font)
        self.info_label_edit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                           "color: rgb(255, 0, 0);")
        self.info_label_edit.setText("")
        self.info_label_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label_edit.setObjectName("info_label_edit")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(169, 80, 371, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.lineEdit_deleteUser = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_deleteUser.setObjectName("lineEdit_deleteUser")
        self.horizontalLayout_7.addWidget(self.lineEdit_deleteUser)
        self.info_label_delete = QtWidgets.QLabel(self.tab_3)
        self.info_label_delete.setGeometry(QtCore.QRect(30, 180, 691, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_label_delete.setFont(font)
        self.info_label_delete.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                             "color: rgb(255, 0, 0);")
        self.info_label_delete.setText("")
        self.info_label_delete.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label_delete.setObjectName("info_label_delete")
        self.pushButton_deleteUser = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_deleteUser.setGeometry(QtCore.QRect(290, 180, 141, 23))
        self.pushButton_deleteUser.setObjectName("pushButton_deleteUser")
        self.info_label_delete_2 = QtWidgets.QLabel(self.tab_3)
        self.info_label_delete_2.setGeometry(QtCore.QRect(40, 40, 691, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_label_delete_2.setFont(font)
        self.info_label_delete_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                               "color: rgb(255, 0, 0);")
        self.info_label_delete_2.setText("")
        self.info_label_delete_2.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label_delete_2.setObjectName("info_label_delete_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(19, 10, 741, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.label_ipAddress = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_ipAddress.setFont(font)
        self.label_ipAddress.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
                                           "color: rgb(255, 0, 0);")
        self.label_ipAddress.setText("")
        self.label_ipAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ipAddress.setObjectName("label_ipAddress")
        self.horizontalLayout_9.addWidget(self.label_ipAddress)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuOptions.addAction(self.actionRefresh)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionLogout)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.spinBox_storage_createUser.setMaximum(100000)

        # actions and events
        self.pushButton_Refresh_view.clicked.connect(self.refreshed_button_pressed)
        self.button_create_user.clicked.connect(self.sql_create_user)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdminPanel"))
        self.table_users.setSortingEnabled(True)
        item = self.table_users.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.table_users.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.table_users.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Storage Size"))
        self.label_11.setText(_translate("MainWindow", "Search for User:"))
        self.pushButton_searchUser_view.setText(_translate("MainWindow", "Search"))
        self.pushButton_Refresh_view.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "View all Users"))
        self.label.setText(_translate("MainWindow", "Username:    "))
        self.label_2.setText(_translate("MainWindow", "Password:     "))
        self.label_3.setText(_translate("MainWindow", "Storage Avaliable:"))
        self.label_4.setText(_translate("MainWindow", "(Mb)"))
        self.button_create_user.setText(_translate("MainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Create User"))
        self.label_5.setText(_translate("MainWindow", "Name of the user to edit:"))
        self.label_6.setText(_translate("MainWindow", "New Username:    "))
        self.label_7.setText(_translate("MainWindow", "New Password:     "))
        self.label_8.setText(_translate("MainWindow", "Change Storage Avaliable for user:"))
        self.label_9.setText(_translate("MainWindow", "(Mb)"))
        self.pushButton_editUser.setText(_translate("MainWindow", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Edit User"))
        self.label_10.setText(_translate("MainWindow", "Username to delete:"))
        self.pushButton_deleteUser.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Delete User"))
        self.label_12.setText(_translate("MainWindow", "Server IP Address:"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.table_users.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def refreshed_button_pressed(self) -> None:
        self.sql_populate_table()
        self.ip_label_update()

    def sql_populate_table(self) -> None:
        """
        Populates the table with users data
        :return: None
        """
        # connection with DB
        db = None
        try:
            db = sqlite3.connect("users.db")
        except Exception as e:
            print(e)

        # SQL commands and cursors
        cursor = db.cursor()
        command = '''SELECT * FROM users'''

        result = cursor.execute(command)
        self.table_users.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table_users.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_users.setItem(row_number, column_number - 1, QTableWidgetItem(str(data)))


    def linecreate_validation(self)-> bool:
        if self.lineEdit_createUsername.text() == "" and self.lineEdit_createPassword.text() == "":
            self.info_label_create.setText("Credentials cant be empty")
            return False
        elif self.lineEdit_createUsername.text() == "":
            self.info_label_create.setText("Please enter a username")
            return False
        elif self.lineEdit_createPassword.text() == "":
            self.info_label_create.setText("Please enter a valid password")
            return False
        elif self.spinBox_storage_createUser.value() == 0:
            self.info_label_create.setText("The minimun storage capacity cant be less than 0")
            return False
        elif self.lineEdit_createUsername.text() != "" and self.lineEdit_createPassword.text() != "" and self.spinBox_storage_createUser.value() != 0:
            return True

    def sql_create_user(self):
        """
        Creates an user from the username and password labes, and the storage capacity from the selection box.
        :return: None
        """
        if self.linecreate_validation():
            create_username = self.lineEdit_createUsername.text()
            create_password = self.lineEdit_createPassword.text()
            create_almacenamiento = int(self.spinBox_storage_createUser.value())
            print(f"{create_username}, {create_password}, {create_almacenamiento}")

            # connection with DB
            db = None
            try:
                db = sqlite3.connect("users.db")
            except Exception as e:
                print(e)

            # SQL commands and cursors
            cmdinsert_create_user = f'''INSERT INTO users(username,password,almacenamiento) values("{create_username}", "{create_password}" , "{create_almacenamiento}");'''
            cmdcheck_create_user = f'''SELECT username FROM users WHERE username = "{create_username}";'''
            cursor = db.cursor()

            #checks if there is another username in use
            cursor.execute(cmdcheck_create_user)
            value = cursor.fetchone()
            if cursor.fetchone():
                msg = QMessageBox()
                msg.setWindowTitle("Username already in use!")
                msg.setText(f"The username you wanted to create already exists! Please use a different username")
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
            else:
                try:
                    print(f"Created the user: {create_username}")
                    cursor.execute(cmdinsert_create_user)
                except Exception as e:
                    print(f"Failed the creationf of user, traceback: {e}")

            db.commit()
            db.close()




    def ip_label_update(self) -> None:
        try:
            server_ip = ip.ip.ip.get_ip()
            self.label_ipAddress.setText(server_ip)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.sql_populate_table()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
