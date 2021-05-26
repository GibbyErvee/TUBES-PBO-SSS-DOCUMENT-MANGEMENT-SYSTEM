# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tampilin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import InsertDocument,InsertTopic,InsertCategory
import Delete
from PyQt5 import QtCore, QtGui, QtWidgets
from prettytable import PrettyTable
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="document_management_system"
)
mycursor = mydb.cursor()


class Ui_CRUD(object):
    def setupUi(self, CRUD):
        CRUD.setObjectName("CRUD")
        CRUD.resize(800, 600)
        CRUD.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(CRUD)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Judul = QtWidgets.QLabel(self.groupBox)
        self.Judul.setGeometry(QtCore.QRect(150, 0, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Judul.setFont(font)
        self.Judul.setAlignment(QtCore.Qt.AlignCenter)
        self.Judul.setObjectName("Judul")
        self.BackIcon = QtWidgets.QLabel(self.groupBox)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("TubesPBO/icon/BackIcon.png"))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 80, 581, 281))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 370, 581, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Insert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Insert.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Insert.setObjectName("Insert")
        self.horizontalLayout.addWidget(self.Insert)
        self.Update = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Update.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Update.setObjectName("Update")
        self.horizontalLayout.addWidget(self.Update)
        self.Delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Delete.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        CRUD.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(CRUD)
        self.statusBar.setObjectName("statusBar")
        CRUD.setStatusBar(self.statusBar)

        self.retranslateUi(CRUD)
        QtCore.QMetaObject.connectSlotsByName(CRUD)

        #code here
        self.Insert.clicked.connect(lambda: self.Masukin(CRUD))
        self.Delete.clicked.connect(lambda: self.Hapusin(CRUD))

    def retranslateUi(self, CRUD):
        _translate = QtCore.QCoreApplication.translate
        CRUD.setWindowTitle(_translate("CRUD", "CRUD"))
        self.Judul.setText(_translate("CRUD", "What do you want"))
        self.Insert.setText(_translate("CRUD", "Insert"))
        self.Update.setText(_translate("CRUD", "Update"))
        self.Delete.setText(_translate("CRUD", "Delete"))

    def Masukin(self,CRUD):
        self.masuk = QtWidgets.QMainWindow()
        if self.M == 1:
            self.ui = InsertDocument.Ui_InsertDocument()
        if self.M == 2:
            self.ui = InsertTopic.Ui_InsertTopic()
        if self.M == 3:
            self.ui = InsertCategory.Ui_MainWindow()
        self.ui.setupUi(self.masuk)
        self.masuk.show()
        CRUD.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Balik(CRUD))

    def Hapusin(self,CRUD):
        self.masuk = QtWidgets.QMainWindow()
        self.ui = Delete.Ui_DeleteWindow()
        self.ui.setupUi(self.masuk)
        self.ui.setUp(self.Judul.text(),self.M)
        self.masuk.show()
        CRUD.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Balik(CRUD))

    def Kerjain(self,order,m):
        try:
            mycursor.execute(order)
            result = mycursor.fetchall()
            if not result:
                result = 'Tidak ada dokumen!'
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

    def Balik(self,CRUD):
        CRUD.show()
        self.masuk.hide()
        if self.M == 1:
            order = f"select * from document"
        if self.M == 2:
            order = f"select * from topic"
        if self.M == 3:
            order = f"select * from category"
        a=self.Kerjain(order,self.M)
        self.plainTextEdit.setPlainText(a)

    def setUp(self,Judul,data):
        if Judul == "Document":
            self.M = 1
        if Judul == "Topic":
            self.M = 2
        if Judul == "Category":
            self.M = 3
        self.Judul.setText(Judul)
        self.plainTextEdit.setPlainText(data)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setStyleSheet('color: rgb(0,0,0);\nbackground-color: rgb(225,225,225);')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CRUD = QtWidgets.QMainWindow()
    ui = Ui_CRUD()
    ui.setupUi(CRUD)
    ui.setUp("Document","Nggak ada\napa-apa")
    CRUD.show()
    sys.exit(app.exec_())
