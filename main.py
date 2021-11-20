import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.addCircle)
        self.circles = []

    def addCircle(self):
        for _ in range(randint(1, 3)):
            r = randint(10, 100)
            x = randint(r, self.width() - r)
            y = randint(r, self.height() - r)
            self.circles.append((x, y, r))
        self.repaint()

    def paintEvent(self, e: QtGui.QPaintEvent):
        super().paintEvent(e)
        if len(self.circles) == 0:
            return

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
        for x, y, r in self.circles:
            qp.drawEllipse(x, y, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
