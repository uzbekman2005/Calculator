from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from calc import *
import sys


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.btn1_clicked)
        self.ui.btn2.clicked.connect(self.btn2_clicked)
        self.ui.btn3.clicked.connect(self.btn3_clicked)
        self.ui.btn4.clicked.connect(self.btn4_clicked)
        self.ui.btn5.clicked.connect(self.btn5_clicked)
        self.ui.btn6.clicked.connect(self.btn6_clicked)
        self.ui.btn7.clicked.connect(self.btn7_clicked)
        self.ui.btn8.clicked.connect(self.btn8_clicked)
        self.ui.btn9.clicked.connect(self.btn9_clicked)
        self.ui.btn0.clicked.connect(self.btn0_clicked)
        self.ui.btnequal.clicked.connect(self.btnEqual_clicked)
        self.ui.btnAc.clicked.connect(self.btnAC_clicked)
        self.ui.btnadd.clicked.connect(self.btnadd_clicked)
        self.ui.btnsub.clicked.connect(self.btnsub_clicked)
        self.ui.btnmul.clicked.connect(self.btnmul_clicked)
        self.ui.btndiv.clicked.connect(self.btndiv_clicked)
        self.ui.btnpercent.clicked.connect(self.btnpercent_clicked)
        self.ui.btnpoint.clicked.connect(self.btnpoint_clicked)
        self.ui.btnabc.clicked.connect(self.btn_abs_clicked)

    def reportErr(self):
        msr = QMessageBox()
        msr.setIcon(QMessageBox.Icon.Information)
        msr.setText("Xato input sodir etildi")
        msr.setWindowTitle("Error!!!")
        msr.setStandardButtons(QMessageBox.StandardButton.Ok)
        res = msr.exec()



    def btn1_clicked(self):
        self.btn_clicked(self, "1")

    def btn2_clicked(self):
        self.btn_clicked(self, "2")

    def btn3_clicked(self):
        self.btn_clicked(self, "3")

    def btn4_clicked(self):
        self.btn_clicked(self, "4")

    def btn5_clicked(self):
        self.btn_clicked(self, "5")

    def btn6_clicked(self):
        self.btn_clicked(self, "6")

    def btn7_clicked(self):
        self.btn_clicked(self, "7")

    def btn8_clicked(self):
        self.btn_clicked(self, "8")

    def btn9_clicked(self):
        self.btn_clicked(self, "9")

    def btn0_clicked(self):
        self.btn_clicked(self, "0")

    def btnEqual_clicked(self):
        try:
            self.ui.labelResult.setText((str(eval(self.ui.labelResult.text()))))
        except Exception as ex:
            self.reportErr()
            self.ui.labelResult.setText("0")
    def btnadd_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-*/.%":
            self.reportErr()
        else:
            self.btn_clicked(self, "+")

    def btnsub_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-*/.%":
            self.reportErr()
        else:
            self.btn_clicked(self, "-")

    def btnmul_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-/.%":
            self.reportErr()
        elif self.ui.labelResult.text()[-2:] == "**":
            self.reportErr()
        else:
            self.btn_clicked(self, "*")

    def btnpercent_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-*/.%":
            self.reportErr()
        else:
            self.btn_clicked(self, "%")

    def btndiv_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-*.%":
            self.reportErr()
        elif self.ui.labelResult.text()[-2:] == "//":
            self.reportErr()
        else:
            self.btn_clicked(self, "/")

    def btnAC_clicked(self):
        self.ui.labelResult.setText("0")

    def btnpoint_clicked(self):
        if self.ui.labelResult.text()[-1] in "+-/*.%":
            self.reportErr()
        else:
            self.btn_clicked(self, ".")

    def btn_abs_clicked(self):
        try:
            self.ui.labelResult.setText(str((float(self.ui.labelResult.text()) * -1)))
        except Exception as ex:
            self.reportErr()
            self.ui.labelResult.setText("0")

    @staticmethod
    def btn_clicked(self, num):
        text = self.ui.labelResult.text()
        if text == "0" and num in ".":
            self.ui.labelResult.setText(text + num)
        elif text == '0' and num in "+-=/*":
            # self.ui.labelResult.setText(num)
            pass
        elif text == "0":
            self.ui.labelResult.setText(num)
        else:
            self.ui.labelResult.setText(text + num)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

