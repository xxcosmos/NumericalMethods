from PyQt5 import QtCore, QtWidgets


class ClassGauss(object):

    def __init__(self, a, b):
        super(ClassGauss, self).__init__()
        self.a = a
        self.b = b
        self.line_num = len(self.b)

    def max(self, line):
        """
        列选主元
        :param line: 当前主元所在的列
        :return: 主元所在的行与值
        """
        max_line = 0
        max_value = self.a[0][0]
        for i in range(line, self.line_num):
            abs_value = abs(self.a[i][line])
            if abs_value > max_value:
                max_value = abs_value
                max_line = i
        return max_line, max_value

    def swap(self, line1, line2):
        """
        换行
        :param line1: 第一行
        :param line2: 第二行
        """
        for row in range(0, self.line_num):
            temp = self.a[line1][row]
            self.a[line1][row] = self.a[line2][row]
            self.a[line2][row] = temp
            temp = self.b[line1]
            self.b[line1] = self.b[line2]
            self.b[line2] = temp

    def gauss(self):
        """
        高斯消元主函数
        :return: 解
        """
        for current_line in range(self.line_num - 1):
            max_line, max_value = self.max(current_line)
            if max_value == 0:
                raise ValueError('无解')

            if max_line != current_line:
                self.swap(max_line, current_line)

            # 归一化
            for row in range(current_line + 1, self.line_num):
                self.a[current_line][row] /= self.a[current_line][current_line]
            self.b[current_line] /= self.a[current_line][current_line]

            # 消元
            for line in range(current_line + 1, self.line_num):
                self.b[line] -= self.a[line][current_line] * self.b[current_line]
                for row in range(current_line + 1, self.line_num):
                    self.a[line][row] -= self.a[line][current_line] * self.a[current_line][row]
        # 回代
        n = self.line_num - 1
        x = [0 for _ in range(n + 2)]
        x[n] = self.b[n] / self.a[n][n]
        for row in range(n - 1, -1, -1):
            res = 0
            for current_line in range(row + 1, n + 1):
                res += self.a[row][current_line] * x[current_line]
            x[row] = (self.b[row] - res)

        ans = ""
        for index in range(self.line_num):
            ans += "x{:d} = {:f}\n".format(index + 1, x[index])
        return ans


class Ui_Dialog(object):
    def __init__(self):
        self.window = QtWidgets.QDialog()
        self.setupUi(self.window)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 240)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 50, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 50, 300, 60))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 72, 15))
        self.label_3.setObjectName("label_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(90, 120, 300, 100))
        self.plainTextEdit_3.setObjectName("plainTextEdit_2")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 10, 101, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(3)
        self.plainTextEdit.setPlainText("2.5 2.3 -5.1 3.7\n5.3 9.6 1.5 3.8\n8.1 1.7 -4.3 5.5")
        self.pushButton.clicked.connect(self.caculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Guass 列选主元消去法"))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.label.setText(_translate("Dialog", "输入\n增广矩阵"))
        self.label_3.setText(_translate("Dialog", "结果"))
        self.label_4.setText(_translate("Dialog", "矩阵的阶"))

    def caculate(self):
        # 2.5 2.3 -5.1 3.7 5.3 9.6 1.5 3.8 8.1 1.7 -4.3 5.5
        num = self.spinBox.value()
        input_matrix = self.plainTextEdit.toPlainText().strip()
        print(input_matrix)
        input_matrix = input_matrix.replace("\n", " ")
        print(input_matrix)

        matrix_a = [[0 for _ in range(num)] for _ in range(num)]
        matrix_b = [0 for _ in range(num)]
        input_str = input_matrix.split(" ")
        for line in range(num):
            for row in range(num + 1):
                if row != num:
                    matrix_a[line][row] = float(input_str[line * (num + 1) + row])
                else:
                    matrix_b[line] = float(input_str[line * (num + 1) + num])

        self.plainTextEdit_3.setPlainText(ClassGauss(matrix_a, matrix_b).gauss())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
