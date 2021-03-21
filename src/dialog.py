# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 333)
        MainWindow.setFixedSize(500, 333)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 450, 291))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.editBtn = QtWidgets.QPushButton(self.widget)
        self.editBtn.setObjectName("editBtn")
        self.gridLayout.addWidget(self.editBtn, 2, 2, 1, 1)
        self.connectBtn = QtWidgets.QPushButton(self.widget)
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout.addWidget(self.connectBtn, 0, 2, 1, 1)
        self.keyInput = QtWidgets.QLineEdit(self.widget)
        self.keyInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyInput.setObjectName("keyInput")
        self.gridLayout.addWidget(self.keyInput, 0, 0, 1, 2)
        self.addBtn = QtWidgets.QPushButton(self.widget)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 2, 0, 1, 1)
        self.deleteBtn = QtWidgets.QPushButton(self.widget)
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout.addWidget(self.deleteBtn, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.btns = [self.connectBtn, self.addBtn, self.editBtn, self.deleteBtn]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passner 0.0.1"))

        self.label.setText(_translate("MainWindow", "Ingresa tu clave maestra para acceder"))
        self.editBtn.setText(_translate("MainWindow", "Editar"))
        self.editBtn.setEnabled(False)
        self.connectBtn.setText(_translate("MainWindow", "Conectar"))
        self.addBtn.setText(_translate("MainWindow", "Agregar"))
        self.deleteBtn.setText(_translate("MainWindow", "Eliminar"))

        for btn in self.btns: btn.setAutoDefault(False)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Usuario"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contraseña"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Información"))
