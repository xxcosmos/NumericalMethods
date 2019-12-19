from math import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.setupUi(self.window)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 499)

        Dialog.setObjectName("centralwidget")
        self.high_limit = QtWidgets.QPlainTextEdit(Dialog)
        self.high_limit.setGeometry(QtCore.QRect(80, 30, 71, 21))
        self.high_limit.setObjectName("high_limit")
        self.function = QtWidgets.QPlainTextEdit(Dialog)
        self.function.setGeometry(QtCore.QRect(30, 120, 421, 74))
        self.function.setObjectName("function")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.low_limit = QtWidgets.QPlainTextEdit(Dialog)
        self.low_limit.setGeometry(QtCore.QRect(230, 30, 71, 21))
        self.low_limit.setObjectName("low_limit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 58, 16))
        self.label_3.setObjectName("label_3")
        self.precision = QtWidgets.QPlainTextEdit(Dialog)
        self.precision.setGeometry(QtCore.QRect(380, 30, 71, 21))
        self.precision.setObjectName("precision")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 161, 16))
        self.label_4.setObjectName("label_4")
        self.output = QtWidgets.QPlainTextEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(30, 280, 421, 151))
        self.output.setObjectName("output")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 58, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 441, 32))
        self.pushButton.setObjectName("pushButton")
        self.function.setPlainText(function)
        self.precision.setPlainText("0.00001")
        self.low_limit.setPlainText("0")
        self.high_limit.setPlainText("1")

        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "变步长梯形法"))
        self.label.setText(_translate("Dialog", "上限："))
        self.label_2.setText(_translate("Dialog", "下限："))
        self.label_3.setText(_translate("Dialog", "精度："))
        self.label_4.setText(_translate("Dialog", "函数：（自变量为 x ）"))
        self.label_5.setText(_translate("Dialog", "输出："))
        self.pushButton.setText(_translate("Dialog", "计算"))

    def calculate(self):
        global function
        function = str(self.function.toPlainText())
        precision = float(self.precision.toPlainText())
        low_limit = float(self.low_limit.toPlainText()) + precision
        high_limit = float(self.high_limit.toPlainText()) + precision
        output = bbctx(low_limit, high_limit, precision)
        self.output.setPlainText(output)


# 变步长梯形法
# 参数：下限，上限，精度
def bbctx(low_limit, high_limit, precision):
    s0 = 0
    s = 5 * (f(low_limit) + f(high_limit)) * (high_limit - low_limit)
    i = 2
    output = ""
    # 循环直到精度符合要求
    while abs(s - s0) > precision:
        h = (high_limit - low_limit) / i
        value = 0
        a = low_limit
        for j in range(i):
            value += 0.5 * (f(a) + f(a + h)) * h
            a += h
        s0 = s
        output += "t[{0}] = {1}\n".format(i, s0)
        s = value
        i *= 2
    return output


def f(x):
    return eval(function)


function = "sin(x)/x"

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
