from PyQt5 import QtCore, QtWidgets
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use("Qt5Agg")


class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)


# Newton 插值法主函数
# data_x 为输入的 x 数组，data_y 为输入的 y 数组，一一对应，x 为 待求值
def newton_interpolation(data_x, data_y, x):
    ans = data_y[0]
    num = len(data_x)
    temp = np.zeros((num, num))
    for i in range(num):
        temp[i, 0] = data_y[i]
    temp_sum = 1.0
    for i in range(1, num):
        temp_sum *= (x - data_x[i - 1])
        # 计算均差
        for j in range(i, num):
            temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (data_x[j] - data_x[j - i])
        ans += temp_sum * temp[i, i]
    return ans




class Ui_Dialog(object):
    def __init__(self):
        self.y = []
        self.x = []
        self.num = 0
        self.window = QtWidgets.QDialog()
        self.setupUi(self.window)
        self.figure = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 455)

        Dialog.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 58, 16))
        self.label.setObjectName("label")
        self.data_number_input = QtWidgets.QPlainTextEdit(Dialog)
        self.data_number_input.setGeometry(QtCore.QRect(100, 20, 120, 21))
        self.data_number_input.setObjectName("data_number_input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 58, 16))
        self.label_2.setObjectName("label_2")
        self.data_input = QtWidgets.QPlainTextEdit(Dialog)
        self.data_input.setGeometry(QtCore.QRect(100, 70, 120, 171))
        self.data_input.setPlaceholderText("")
        self.data_input.setObjectName("data_input")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 58, 16))
        self.label_3.setObjectName("label_3")
        self.x_input = QtWidgets.QPlainTextEdit(Dialog)
        self.x_input.setGeometry(QtCore.QRect(100, 270, 120, 21))
        self.x_input.setObjectName("x_input")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 310, 210, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 360, 58, 16))
        self.label_4.setObjectName("label_4")
        self.y_output = QtWidgets.QPlainTextEdit(Dialog)
        self.y_output.setEnabled(True)
        self.y_output.setGeometry(QtCore.QRect(100, 360, 120, 21))
        self.y_output.setObjectName("y_output")

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 20, 331, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.figure_output = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.figure_output.setContentsMargins(0, 0, 0, 0)
        self.figure_output.setObjectName("figure_output")

        self.data_number_input.setPlainText("4")
        self.data_input.setPlainText("0.56160 0.82741\n0.56280 0.82659\n0.56401 0.82577\n0.56521 0.82495")
        self.x_input.setPlainText("0.5635")

        self.pushButton.clicked.connect(self.calculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "牛顿插值法"))
        self.label.setText(_translate("Dialog", "数据个数："))
        self.label_2.setText(_translate("Dialog", "数据："))
        self.label_3.setText(_translate("Dialog", "待求值 X："))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.label_4.setText(_translate("Dialog", "近似值 Y："))

    def draw(self):
        figure = MyFigure(3, 3, 100)
        axes = figure.fig.add_subplot(111)

        x = sorted(self.x)
        xx = np.arange(x[0], x[self.num - 1] + 0.1, 0.1)

        yy = [[0] for _ in range(0, len(xx))]
        for i in range(0, len(xx)):
            # yy[i] = calculate_answer(x, self.y, xx[i])
            yy[i] = newton_interpolation(x, self.y, xx[i])

        axes.plot(xx, np.array(yy))
        figure.fig.suptitle("Newton")
        if self.figure is not None:
            self.figure_output.removeWidget(self.figure)
        self.figure_output.addWidget(figure)
        self.figure = figure

    def calculate(self):
        self.num = int(self.data_number_input.toPlainText())
        parameter = float(self.x_input.toPlainText())
        data = str(self.data_input.toPlainText()).split("\n")
        self.x = []
        self.y = []
        for row in data:
            row = row.split(" ")
            self.x.append(float(row[0]))
            self.y.append(float(row[1]))
        self.draw()

        # ans = calculate_answer(self.x, self.y, parameter)
        ans = newton_interpolation(self.x, self.y, parameter)
        self.y_output.setPlainText(str(round(ans, 5)))