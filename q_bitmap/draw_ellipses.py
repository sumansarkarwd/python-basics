import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QPoint, QRect

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
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawEllipse(QPoint(100, 100), 10, 10)
        painter.drawEllipse(QPoint(100, 100), 20, 15)
        painter.drawEllipse(QPoint(100, 100), 30, 20)
        painter.drawEllipse(QPoint(100, 100), 40, 25)

        painter.end()



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
