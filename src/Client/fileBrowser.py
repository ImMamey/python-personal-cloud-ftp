from PyQt5 import QtWidgets, QtGui, QtCore

from ui import main


class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.populate()

    def populate(self):
        path = "C:\Windows"
        model = QtWidgets.QFileSystemModel()
        model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path))
        self.treeView.setSortingEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
