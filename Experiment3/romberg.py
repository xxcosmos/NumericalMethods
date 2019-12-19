import numpy as np
import sys
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets

np.set_printoptions(precision=8, linewidth=120)


def f(x):
    return eval(function)


function = "sin(x)/x"


# 龙贝格法 主函数
def integrate(low_limit, high_limit):
    steps = 8
    table = np.zeros((steps, steps), dtype=np.float64)
    pow_4 = 4 ** np.arange(steps, dtype=np.float64) - 1
    # 梯形规则
    h = (high_limit - low_limit)
    table[0, 0] = h * (f(low_limit) + f(high_limit)) / 2
    for j in range(1, steps):
        h /= 2
        # 拓展梯形规则
        table[j, 0] = table[j - 1, 0] / 2
        table[j, 0] += h * sum(
            f(low_limit + i * h) for i in range(1, 2 ** j + 1, 2)
        )
        # 理查森外推法
        for k in range(1, j + 1):
            table[j, k] = table[j, k - 1] + (table[j, k - 1] - table[j - 1, k - 1]) / pow_4[k]

    output = "结果：" + str(table[-1, -1])
    output += "\n" + str(table)
    return output


class Ui_Dialog(object):
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.setupUi(self.window)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 662)

        Dialog.setObjectName("centralwidget")
        self.high_limit = QtWidgets.QPlainTextEdit(Dialog)
        self.high_limit.setGeometry(QtCore.QRect(190, 30, 71, 21))
        self.high_limit.setObjectName("high_limit")
        self.function = QtWidgets.QPlainTextEdit(Dialog)
        self.function.setGeometry(QtCore.QRect(140, 120, 421, 74))
        self.function.setObjectName("function")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 30, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.low_limit = QtWidgets.QPlainTextEdit(Dialog)
        self.low_limit.setGeometry(QtCore.QRect(340, 30, 71, 21))
        self.low_limit.setObjectName("low_limit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 30, 58, 16))
        self.label_3.setObjectName("label_3")
        self.precision = QtWidgets.QPlainTextEdit(Dialog)
        self.precision.setGeometry(QtCore.QRect(490, 30, 71, 21))
        self.precision.setObjectName("precision")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 90, 161, 16))
        self.label_4.setObjectName("label_4")
        self.output = QtWidgets.QPlainTextEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(30, 280, 661, 291))
        self.output.setObjectName("output")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 58, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 210, 441, 32))
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
        Dialog.setWindowTitle(_translate("Dialog", "龙贝格法"))
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
        output = integrate(low_limit, high_limit)
        self.output.setPlainText(output)
