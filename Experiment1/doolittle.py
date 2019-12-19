from PyQt5 import QtCore, QtWidgets


# [1, -1, 3,] [2,-4,6] [4,-9,2]
# [2,10,0,-3] [-3,-4,-12,13] [4,14,9,-13]
def doolittle(matrix, num):
    """
    Doolittle 三角分解
    :param matrix: 求解矩阵
    :param num: 矩阵的阶
    :return: 结果
    """
    # 计算 L 的第一列
    for line in range(2, num + 1):
        matrix[line][1] = matrix[line][1] / matrix[1][1]

    for r in range(2, num + 1):
        # 计算 U 的 r 行
        for j in range(r, num + 1):
            for k in range(1, r):
                matrix[r][j] -= matrix[r][k] * matrix[k][j]
        # 计算 L 的 r 列
        for j in range(r + 1, num + 1):
            for k in range(1, r):
                matrix[j][r] -= matrix[j][k] * matrix[k][r]
            matrix[j][r] = matrix[j][r] / matrix[r][r]

    res = ""
    for line in range(1, num + 1):
        res += "["
        for j in range(1, num + 1):
            res += "{:+.4f}".format(matrix[line][j])
            res += " "
        res += "]\n"
    return res


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
        self.textEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 50, 300, 60))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 72, 15))
        self.label_3.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 120, 300, 100))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 10, 101, 21))
        self.spinBox.setObjectName("spinBox")

        self.spinBox.setValue(3)
        self.textEdit.setPlainText("[2,10,0,-3]\n[-3,-4,-12,13]\n[4,14,9,-13]")
        self.pushButton.clicked.connect(self.work)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Doolittle 三角分解法"))
        self.pushButton.setText(_translate("Dialog", "计算"))
        self.label.setText(_translate("Dialog", "输入数据"))
        self.label_3.setText(_translate("Dialog", "结果"))
        self.label_4.setText(_translate("Dialog", "矩阵的阶"))

    def work(self):
        # [,,,] [,,,] [,,,]
        num = self.spinBox.value()
        input_matrix = self.textEdit.toPlainText().strip("\n")

        matrixa = [[0 for _ in range(num + 2)] for _ in range(num + 2)]

        str = input_matrix.split("]", num - 1)

        for i in range(num):
            for j in range(num):
                if j != num - 1:
                    matrixa[i + 1][j + 1] = float(str[i].split("[")[1].split(",")[j])
                else:
                    matrixa[i + 1][j + 1] = float(str[i].split("[")[1].split(",")[j].split("]")[0])

        ans = doolittle(matrixa, num)
        self.textEdit_3.setPlainText(ans)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
