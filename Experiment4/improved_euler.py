function = "-x*y*y"


def f(x, y):
    return eval(function)


def improved_euler(a=0, b=1, ya=1, h=0.1):
    '''改进欧拉法'''
    xi = a
    yi = ya
    res = ""
    while xi <= b:  # 在求解区间范围
        yp = yi + h * f(xi, yi)
        y = yi + h / 2 * (f(xi, yi) + f(xi, yp))

        res += 'xi:{:.2f}, yi:{:.6f}\n'.format(xi, yi)

        xi, yi = xi + h, y

    return res


from PyQt5 import QtCore, QtGui, QtWidgets


class Improved_euler(object):
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.setupUi(self.window)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 637)


        Dialog.setObjectName("centralwidget")
        self.start_value = QtWidgets.QPlainTextEdit(Dialog)
        self.start_value.setGeometry(QtCore.QRect(120, 10, 71, 21))
        self.start_value.setObjectName("start_value")
        self.function = QtWidgets.QPlainTextEdit(Dialog)
        self.function.setGeometry(QtCore.QRect(30, 120, 351, 74))
        self.function.setObjectName("function")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 20))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 161, 16))
        self.label_4.setObjectName("label_4")
        self.output = QtWidgets.QPlainTextEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(30, 280, 351, 291))
        self.output.setObjectName("output")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 58, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 371, 32))
        self.pushButton.setObjectName("pushButton")
        self.end_value = QtWidgets.QPlainTextEdit(Dialog)
        self.end_value.setGeometry(QtCore.QRect(310, 10, 71, 21))
        self.end_value.setObjectName("end_value")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 71, 20))
        self.label_2.setObjectName("label_2")
        self.init_value = QtWidgets.QPlainTextEdit(Dialog)
        self.init_value.setGeometry(QtCore.QRect(120, 40, 71, 21))
        self.init_value.setObjectName("init_value")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 71, 20))
        self.label_3.setObjectName("label_3")
        self.path_length = QtWidgets.QPlainTextEdit(Dialog)
        self.path_length.setGeometry(QtCore.QRect(310, 40, 71, 21))
        self.path_length.setObjectName("path_length")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 40, 71, 20))
        self.label_6.setObjectName("label_6")

        self.start_value.setPlainText("0")
        self.function.setPlainText(function)
        self.init_value.setPlainText("2")
        self.end_value.setPlainText("5")
        self.path_length.setPlainText("0.25")

        self.pushButton.clicked.connect(self.calculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "改进欧拉法"))
        self.label.setText(_translate("Dialog", "区间起始值："))
        self.label_4.setText(_translate("Dialog", "函数：（自变量为 x ）"))
        self.label_5.setText(_translate("Dialog", "输出："))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.label_2.setText(_translate("Dialog", "区间终点值："))
        self.label_3.setText(_translate("Dialog", "起始条件："))
        self.label_6.setText(_translate("Dialog", "步长："))

    def calculate(self):
        global function
        function = str(self.function.toPlainText())
        ya = int(self.init_value.toPlainText())
        a = int(self.start_value.toPlainText())
        b = int(self.end_value.toPlainText())
        h = float(self.path_length.toPlainText())
        output = improved_euler(a, b, ya, h)
        self.output.setPlainText(output)