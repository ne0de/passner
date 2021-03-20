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
        self.fileManager.search()

        self.ui.connectBtn.clicked.connect(self.verifyKeyMaster)
    
    def verifyKeyMaster(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassnerApp()
    window.show()
    sys.exit(app.exec_())