from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QStandardItem, QStandardItemModel
import os
from ui import main
from ftplib import FTP

#TODO: these details needs to be deleted later on, the credential cant be stored in this program
host = "192.168.0.101"
user = "user"
password = "12345"
ftp_list = []

class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

        self.tree_model = QStandardItemModel()




    def populate(self):
        ftp_list = self.basicConnection()

        files = QStandardItem()

        for _ in ftp_list:
            item = QStandardItem(str(ftp_list[_]), 16, set_bold=True)
            files.appendRow(item)


        self.model = self.tree_model
        self.treeView.setModel(self.model)

        #path = "C:\Windows"
        #self.model = QtWidgets.QFileSystemModel()
        #self.model.setRootPath((QtCore.QDir.rootPath()))
        #self.treeView.setModel(self.model)
        #self.treeView.setRootIndex(self.model.index(path))
        #self.treeView.setSortingEnabled(True)
        print()

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def _set_current_item(self,list_type,filename):
        '''
        :param list_type: local or remote
        :param filename:
        :return:
        '''

        file_list = self.Local_Filelist if list_type == 'local' else self.Remote_FileList
        total_file = file_list.topLevelItemCount()
        for i in range(total_file):
            if file_list.topLevelItemCount(i).text(0) == filename:
                file_list.setCurrentItem(file_list.topLevelItem(i))
                break

    def basicConnection(self) -> list:
        # TODO for not local host, the bellow line should use the "host" variable
        with FTP("localhost", timeout=30) as ftp:
            ftp.connect(host, 2121)
            ftp.login(user=user, passwd=password)
            print(ftp.getwelcome())

            targetfile = 'hllo.txt'
            localfilepath = targetfile

            ftp.nlst()
            # with open('test.txt', 'wb') as f:
            #    retCode = ftp.retrbinary(f"RETR {targetfile}", f.write, 1024)
            # show files in the cwd

            ftp_list = ftp.nlst()
            for _ in ftp_list:
                print(_)

            return list

            ftp.quit()



#with FTP(host) as ftp:
#    ftp.login(user=user, passwd=password)
#    print(ftp.getwelcome())
#
#    with open()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
