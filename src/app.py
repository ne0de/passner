#! /usr/bin/python3

import sys, ctypes, platform, os
from passlib.hash import pbkdf2_sha256
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5 import QtCore
from dialog import Ui_MainWindow
from fileManager import PassnerFileManager
from database import PassnerDatabase
from cryptography.fernet import Fernet 

class PassnerApp(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Fernet.generate_key()

        self.connected = False
        self.messageInformer = QMessageBox()
        self.fileManager = PassnerFileManager()
        self.database = PassnerDatabase(self.fileManager.getDir() + '/data.db')

        self.temp = dict()
        self.ui.addBtn.clicked.connect(self.addUsername)
        self.ui.connectBtn.clicked.connect(self.connect)

        self.verifyDirectory()
        self.verifyDatabase()
        self.verifyKeyMaster()
    
    def showMessage(self, title, msg, ty, desc=None):
        if desc != None:  self.messageInformer.setInformativeText(desc)
        self.messageInformer.setIcon(ty)
        self.messageInformer.setText(msg)
        self.messageInformer.setFixedHeight(400)
        self.messageInformer.setFixedWidth(400)
        self.messageInformer.setWindowTitle(title)
        self.messageInformer.exec_()
        self.messageInformer.setInformativeText('')
    
    def verifyKeyMaster(self):
        if not self.database.getKeyMaster():
            key, r = QInputDialog.getText(self, 'Clave maestra', 'Escribe la clave maestra que usaras para la aplicación', echo = QLineEdit.Password)
            if not r: return sys.exit(self.app.exec_())
            if not bool(key): return self.verifyKeyMaster()
            self.database.addKeyMaster(pbkdf2_sha256.hash(key) + str(Fernet.generate_key()))
        else:
            print(self.database.getKeyMaster()[0])
            print(self.database.getKeyMaster()[1])
            

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
    
    def addUsername(self):
        if not self.connected: return self.showMessage('Error', 'No hay conexión', QMessageBox.Warning, 'Conectate con tu clave maestra')
        else:
            username, r = QInputDialog.getText(self, 'Usuario', 'Especifica el nombre de usuario')
            if not r or not bool(username): return False
            self.temp['username'] = username
            return self.addPassword()

    def addPassword(self):
        password, r = QInputDialog.getText(self, 'Contraseña', 'Especifica la contraseña', echo = QLineEdit.Password)
        if not r or not bool(password): return False
        self.temp['password'] = password
        return self.addInformation()
    
    def addInformation(self):
        text, r = QInputDialog.getText(self, 'Informacion', 'Especifica de donde proviene esta cuenta')
        if not r or not bool(password): return False
        self.temp['info'] = text
        self.database.addAccount(self.temp)
    
    def connect(self):
        self.connected = self.database.createConnection()
        key = self.database.getKeyMaster()[0]

        match = pbkdf2_sha256.verify(self.ui.keyInput.text(), key)
        self.ui.keyInput.setText('')
        if not match:
            self.connected = False
            self.database.closeConnection()
            return self.showMessage('Error', 'Clave maestra incorrecta', QMessageBox.Warning)
        self.showMessage('Info', 'Te has conectado correctamente', QMessageBox.Information)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassnerApp(app)
    window.show()
    sys.exit(app.exec_())