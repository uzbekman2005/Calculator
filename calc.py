# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(409, 496)
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(51, 209, 122);\n"
"background-color: rgb(98, 160, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(0, 0, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.labelResult.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelResult.setObjectName("labelResult")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 170, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn7.setObjectName("btn7")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(110, 250, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 250, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn4.setObjectName("btn4")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(210, 170, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn9.setObjectName("btn9")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(110, 170, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn8.setObjectName("btn8")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(110, 330, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 330, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn1.setObjectName("btn1")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(210, 250, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn6.setObjectName("btn6")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(210, 330, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn3.setObjectName("btn3")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(10, 410, 181, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(249, 240, 107);")
        self.btn0.setObjectName("btn0")
        self.btnpoint = QtWidgets.QPushButton(self.centralwidget)
        self.btnpoint.setGeometry(QtCore.QRect(210, 410, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btnpoint.setFont(font)
        self.btnpoint.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"color: rgb(255, 255, 255);")
        self.btnpoint.setObjectName("btnpoint")
        self.btnpercent = QtWidgets.QPushButton(self.centralwidget)
        self.btnpercent.setGeometry(QtCore.QRect(210, 110, 85, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnpercent.setFont(font)
        self.btnpercent.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btnpercent.setObjectName("btnpercent")
        self.btnabc = QtWidgets.QPushButton(self.centralwidget)
        self.btnabc.setGeometry(QtCore.QRect(110, 110, 85, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnabc.setFont(font)
        self.btnabc.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btnabc.setObjectName("btnabc")
        self.btnAc = QtWidgets.QPushButton(self.centralwidget)
        self.btnAc.setGeometry(QtCore.QRect(10, 110, 85, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnAc.setFont(font)
        self.btnAc.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(255, 255, 255);")
        self.btnAc.setObjectName("btnAc")
        self.btnmul = QtWidgets.QPushButton(self.centralwidget)
        self.btnmul.setGeometry(QtCore.QRect(310, 170, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btnmul.setFont(font)
        self.btnmul.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.btnmul.setObjectName("btnmul")
        self.btnadd = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd.setGeometry(QtCore.QRect(310, 250, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btnadd.setFont(font)
        self.btnadd.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.btnadd.setObjectName("btnadd")
        self.btnsub = QtWidgets.QPushButton(self.centralwidget)
        self.btnsub.setGeometry(QtCore.QRect(310, 330, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btnsub.setFont(font)
        self.btnsub.setStyleSheet("background-color: rgb(181, 131, 90);\n"
"border-color: rgb(224, 27, 36);")
        self.btnsub.setObjectName("btnsub")
        self.btnequal = QtWidgets.QPushButton(self.centralwidget)
        self.btnequal.setGeometry(QtCore.QRect(310, 410, 85, 70))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.btnequal.setFont(font)
        self.btnequal.setStyleSheet("background-color: rgb(73, 168, 53);")
        self.btnequal.setObjectName("btnequal")
        self.btndiv = QtWidgets.QPushButton(self.centralwidget)
        self.btndiv.setGeometry(QtCore.QRect(310, 110, 85, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btndiv.setFont(font)
        self.btndiv.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.btndiv.setObjectName("btndiv")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.labelResult.setText(_translate("MainWindow", "0"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnpoint.setText(_translate("MainWindow", "."))
        self.btnpercent.setText(_translate("MainWindow", "%"))
        self.btnabc.setText(_translate("MainWindow", "+/-"))
        self.btnAc.setText(_translate("MainWindow", "AC"))
        self.btnmul.setText(_translate("MainWindow", "*"))
        self.btnadd.setText(_translate("MainWindow", "+"))
        self.btnsub.setText(_translate("MainWindow", "-"))
        self.btnequal.setText(_translate("MainWindow", "="))
        self.btndiv.setText(_translate("MainWindow", "/"))
