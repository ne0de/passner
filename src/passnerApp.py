import sys
from PyQt5.QtWidgets import QApplication, QDialog
from passnerDialog import Ui_MainWindow

class PassnerApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassnerApp()
    window.show()
    sys.exit(app.exec_())