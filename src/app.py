#! /usr/bin/python3

import sys, ctypes, platform, os

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtCore import QCoreApplication
from dialog import Ui_MainWindow
from fileManager import PassnerFileManager
from database import PassnerDatabase

class PassnerApp(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.messageInformer = QMessageBox()
        self.fileManager = PassnerFileManager()
        self.database = PassnerDatabase(self.fileManager.getDir() + '/data.db')

        self.ui.connectBtn.clicked.connect(self.connect)
        self.verifyDirectory()
        self.verifyDatabase()
        self.verifyKeyMaster()
    
    def showMessage(self, title, msg, ty, desc=None):
        if desc != None:  self.messageInformer.setInformativeText(desc)
        self.messageInformer.setIcon(ty)
        self.messageInformer.setText(msg)
        self.messageInformer.setWindowTitle(title)
        self.messageInformer.exec_()

    def prepare(self):
        pass
    
    def verifyKeyMaster(self):
        if not self.database.existKeyMaster():
            key, r = QInputDialog.getText(self, 'Clave maestra', 'Escribe la clave maestra que usaras para la aplicación', echo = QLineEdit.Password)
            if not r: return sys.exit(self.app.exec_())
            if not bool(key): return self.verifyKeyMaster()
            self.database.addKeyMaster(key)
        else: 
            pass

    def verifyDatabase(self):
        self.database.createConnection()
        if not self.database.existTables(): 
            self.database.createTables()
        else:
            pass
        
    def verifyDirectory(self):
        if not self.fileManager.existDir():
            res, msg = self.fileManager.createDir()
            if not res: 
                self.showMessage('Error', str(msg), QMessageBox.Critical, 'No se pudo acceder a los archivos internos')
                sys.exit(app.exec_())
    
    def connect(self):
        self.verifyDirectory()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassnerApp(app)
    window.show()
    sys.exit(app.exec_())