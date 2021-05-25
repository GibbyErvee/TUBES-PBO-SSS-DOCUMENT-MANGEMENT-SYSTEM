# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tampilin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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

    def retranslateUi(self, CRUD):
        _translate = QtCore.QCoreApplication.translate
        CRUD.setWindowTitle(_translate("CRUD", "CRUD"))
        self.Judul.setText(_translate("CRUD", "What do you want"))
        self.Insert.setText(_translate("CRUD", "Insert"))
        self.Update.setText(_translate("CRUD", "Update"))
        self.Delete.setText(_translate("CRUD", "Delete"))

    def setUp(self,Judul,data):
        self.Judul.setText(Judul)
        self.plainTextEdit.setPlainText(data)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CRUD = QtWidgets.QMainWindow()
    ui = Ui_CRUD()
    ui.setupUi(CRUD)
    ui.setUp("Percobaan","Nggak ada\napa-apa")
    CRUD.show()
    sys.exit(app.exec_())
