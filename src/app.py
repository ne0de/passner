import sys, platform
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from dialog import Ui_MainWindow
from fileManager import PassnerFileManager

class PassnerApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.messageInformer = QMessageBox()
        self.fileManager = PassnerFileManager()

        self.ui.connectBtn.clicked.connect(self.verifyKeyMaster)
    
    def showMessage(self, msg, tittle):
        self.messageInformer.setText(msg)
        self.messageInformer.setIcon(QMessageBox.Critical)
        self.messageInformer.setWindowTitle(tittle)
        self.messageInformer.exec_()

    def verifyKeyMaster(self):
        if not self.fileManager.existDir():
            res, msg = self.fileManager.createDir()
            if not res: self.showMessage(str(msg), 'Error')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassnerApp()
    window.show()
    sys.exit(app.exec_())