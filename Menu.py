# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Tampilin
from prettytable import PrettyTable
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="document_management_system"
)
mycursor = mydb.cursor()


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        Menu.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 40, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 581, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.documentbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.documentbutton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.documentbutton.setObjectName("documentbutton")
        self.verticalLayout.addWidget(self.documentbutton)
        self.Topic = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Topic.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Topic.setObjectName("Topic")
        self.verticalLayout.addWidget(self.Topic)
        self.categorybutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.categorybutton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.categorybutton.setObjectName("categorybutton")
        self.verticalLayout.addWidget(self.categorybutton)
        self.BackIcon = QtWidgets.QLabel(self.groupBox)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("C:/Users/acer/.designer/backup/icon/LogOut.png"))
        self.BackIcon.setScaledContents(True)
        self.BackIcon.setObjectName("BackIcon")
        self.BackButton = QtWidgets.QPushButton(self.groupBox)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setKerning(False)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BackButton.setMouseTracking(False)
        self.BackButton.setAutoFillBackground(False)
        self.BackButton.setStyleSheet("color: rgb(170, 255, 255);\n"
"background-color: transparent;\n"
"")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        #code here
        self.documentbutton.clicked.connect(lambda: self.NampilinDokumen(Menu))
        self.Topic.clicked.connect(lambda: self.NampilinTopik(Menu))
        self.categorybutton.clicked.connect(lambda: self.NampilinKategori(Menu))

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "Menu"))
        self.documentbutton.setText(_translate("Menu", "Document"))
        self.Topic.setText(_translate("Menu", "Topic"))
        self.categorybutton.setText(_translate("Menu", "Category"))

    def NampilinDokumen(self, Menu):
        order = f"select * from document"
        a = self.kerjain(order,1)
        self.pindah(Menu,"Document",a)

    def NampilinTopik(self, Menu):
        order = f"select * from topic"
        a = self.kerjain(order,2)
        self.pindah(Menu,"Topic",a)

    def NampilinKategori(self, Menu):
        order = f"select * from category"
        a = self.kerjain(order,3)
        self.pindah(Menu,"Category",a)

    def kerjain(self,order,m):
        try:
            mycursor.execute(order)
            result = mycursor.fetchall()
            if not result:
                result = 'Belum ada dokumen'
            else:
                if m==1:
                    a=PrettyTable(['document_id','category_id','topic_id','Tag','file_name'])
                if m==2:
                    a=PrettyTable(['topic_id','topic','storage_file'])
                if m==3:
                    a=PrettyTable(['category_id','name'])
                for i in result:
                    a.add_row(i)
                result = str(a)
        except mysql.connector.Error as error:
            result = 'Error, error code: ' + str(error)

        return result

    def pindah(self, Menu, Judul, Data):
        self.Nampilin = QtWidgets.QMainWindow()
        self.ui = Tampilin.Ui_CRUD()
        self.ui.setupUi(self.Nampilin)
        self.ui.setUp(Judul,Data)
        self.Nampilin.show()
        Menu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Balik(Menu))

    def Balik(self,Menu):
        self.Nampilin.hide()
        Menu.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
