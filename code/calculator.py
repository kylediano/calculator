from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        super(object).__init__()
        self.output = "0"
        self.num1 = ""
        self.num2 = ""
        self.operator = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 491)
        MainWindow.setFixedSize(390, 491)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/calculator-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(30, 70, 331, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.screen.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pro H")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.screen.setFont(font)
        self.screen.setAutoFillBackground(False)
        self.screen.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen.setLineWidth(3)
        self.screen.setMidLineWidth(0)
        self.screen.setTextFormat(QtCore.Qt.PlainText)
        self.screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.screen.setObjectName("screen")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(40, 230, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(120, 230, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.button_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.button_decimal.setGeometry(QtCore.QRect(200, 390, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_decimal.setFont(font)
        self.button_decimal.setObjectName("button_decimal")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(120, 390, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.button_sign = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign.setGeometry(QtCore.QRect(40, 390, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_sign.setFont(font)
        self.button_sign.setObjectName("button_sign")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(120, 340, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(200, 340, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(200, 230, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(40, 340, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(200, 290, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(120, 290, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(40, 290, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(280, 340, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.button_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.button_subtract.setGeometry(QtCore.QRect(280, 290, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_subtract.setFont(font)
        self.button_subtract.setObjectName("button_subtract")
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiply.setGeometry(QtCore.QRect(280, 230, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_multiply.setFont(font)
        self.button_multiply.setObjectName("button_multiply")
        self.button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.button_divide.setGeometry(QtCore.QRect(280, 170, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_divide.setFont(font)
        self.button_divide.setObjectName("button_divide")
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setGeometry(QtCore.QRect(280, 390, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_equals.setFont(font)
        self.button_equals.setObjectName("button_equals")
        self.button_bksp = QtWidgets.QPushButton(self.centralwidget)
        self.button_bksp.setGeometry(QtCore.QRect(200, 170, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_bksp.setFont(font)
        self.button_bksp.setObjectName("button_bksp")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(120, 170, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.button_sq = QtWidgets.QPushButton(self.centralwidget)
        self.button_sq.setGeometry(QtCore.QRect(40, 170, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_sq.setFont(font)
        self.button_sq.setObjectName("button_sq")
        MainWindow.setCentralWidget(self.centralwidget)

        self.operation = QtWidgets.QLabel(self.centralwidget)
        self.operation.setGeometry(QtCore.QRect(300, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N B")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.operation.setFont(font)
        self.operation.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.operation.setObjectName("operation")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_clear.clicked.connect(self.clear_output)

        self.button_bksp.clicked.connect(self.backspace)

        self.button_sign.clicked.connect(self.change_sign)
        self.button0.clicked.connect(lambda: self.input_num("0"))
        self.button1.clicked.connect(lambda: self.input_num("1"))
        self.button2.clicked.connect(lambda: self.input_num("2"))
        self.button3.clicked.connect(lambda: self.input_num("3"))
        self.button4.clicked.connect(lambda: self.input_num("4"))
        self.button5.clicked.connect(lambda: self.input_num("5"))
        self.button6.clicked.connect(lambda: self.input_num("6"))
        self.button7.clicked.connect(lambda: self.input_num("7"))
        self.button8.clicked.connect(lambda: self.input_num("8"))
        self.button9.clicked.connect(lambda: self.input_num("9"))
        self.button_decimal.clicked.connect(lambda: self.input_num("."))

        self.button_sq.clicked.connect(self.squared)
        self.button_add.clicked.connect(lambda: self.set_operator("+"))
        self.button_subtract.clicked.connect(lambda: self.set_operator("-"))
        self.button_divide.clicked.connect(lambda: self.set_operator("/"))
        self.button_multiply.clicked.connect(lambda: self.set_operator("*"))
        self.button_equals.clicked.connect(self.equals)

    def clear_output(self):
        self.output = "0"
        self.screen.setText(self.output)

    def set_operator(self, op):
        if self.operator == "":
            self.operator = op
            self.num1 = self.output
            self.output = "0"
        else:
            self.operator = op
        self.operation.setText(self.operator)

    def squared(self):
        num = float(self.output)
        sq = num * num
        if len(self.output) == 13:
            pass
        else:
            if len(str(sq)) > 13:
                self.screen.setText("ERROR")
                self.output = "0"
            else:
                self.output = str(sq)
                self.screen.setText(self.output)
            if "." in self.output and self.output[-1] == "0":
                self.output = self.output.split('.')[0]
                self.screen.setText(self.output)
            else:
                pass

    def equals(self):
        if self.operator != "":
            self.num2 = self.output
            answer = 0
            if self.operator == "+":
                answer = float(self.num1) + float(self.num2)
            elif self.operator == "-":
                answer = float(self.num1) - float(self.num2)
            elif self.operator == "/":
                answer = float(self.num1) / float(self.num2)
            elif self.operator == "*":
                answer = float(self.num1) * float(self.num2)
            if len(str(answer)) > 13:
                self.screen.setText("ERROR")
                self.output = "0"
            else:
                self.output = str(answer)
                self.screen.setText(self.output)
            if "." in self.output and self.output[-1] == "0":
                self.output = self.output.split('.')[0]
                self.screen.setText(self.output)
            else:
                pass
            self.num1 = ""
            self.num2 = ""
            self.operator = ""
            self.operation.setText(self.operator)

    def backspace(self):
        if len(self.output) > 1:
            self.output = self.output[:-1]
            self.screen.setText(self.output)
        else:
            self.output = "0"
            self.screen.setText(self.output)

    def change_sign(self):
        if self.output != "0":
            if len(self.output) < 12:
                if self.output[0] == "-":
                    self.output = self.output[1:]
                    self.screen.setText(self.output)
                else:
                    self.output = "-" + self.output
                    self.screen.setText(self.output)
        else:
            pass

    def input_num(self, num):
        if num == ".":
            if self.output == "0":
                self.output = self.output + num
                self.screen.setText(self.output)
            elif "." in self.output:
                pass
            elif len(self.output) < 12:
                self.output += num
            else:
                pass
        else:
            if len(self.output) < 12:
                if self.output == "0":
                    self.output = num
                    self.screen.setText(self.output)
                else:
                    self.output += num
                    self.screen.setText(self.output)
            else:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kyle\'s Calculator"))
        self.screen.setText(_translate("MainWindow", "0"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button_decimal.setText(_translate("MainWindow", "."))
        self.button0.setText(_translate("MainWindow", "0"))
        self.button_sign.setText(_translate("MainWindow", "+/−"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_subtract.setText(_translate("MainWindow", "−"))
        self.button_multiply.setText(_translate("MainWindow", "×"))
        self.button_divide.setText(_translate("MainWindow", "÷"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_bksp.setText(_translate("MainWindow", "⌫"))
        self.button_clear.setText(_translate("MainWindow", "CE"))
        self.button_sq.setText(_translate("MainWindow", "x²"))
        self.operation.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
