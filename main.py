import sys
from PyQt5 import QtGui
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Form(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addCircle)
        self.circles = []

    def addCircle(self):
        for _ in range(randint(1, 3)):
            r = randint(10, 100)
            x = randint(r, self.width() - r)
            y = randint(r, self.height() - r)
            c = (randint(100, 255), randint(100, 255), randint(100, 255))
            self.circles.append((x, y, r, c))
        self.repaint()

    def paintEvent(self, e: QtGui.QPaintEvent):
        super().paintEvent(e)
        if len(self.circles) == 0:
            return

        qp = QtGui.QPainter()
        qp.begin(self)
        for x, y, r, c in self.circles:
            qp.setPen(QtGui.QPen(QtGui.QColor(*c), 2))
            qp.drawEllipse(x, y, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())

