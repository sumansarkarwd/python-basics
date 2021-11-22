import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QRect, Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    def draw_something(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('red'))
        pen.setWidth(5)
        painter.setPen(pen)

        painter.drawRect(QRect(10, 10, 100, 100))

        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawRect(20, 20, 200, 200)

        # draw multiple rectangles at once
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        painter.drawRects(
            QRect(30, 30, 100, 100),
            QRect(40, 40, 200, 200),
            QRect(50, 50, 250, 250),
        )

        # fill rect with color
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('yellow'))
        brush.setStyle(Qt.Dense1Pattern)
        # brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        painter.drawRect(QRect(60, 100, 100, 140))

        painter.end()



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
