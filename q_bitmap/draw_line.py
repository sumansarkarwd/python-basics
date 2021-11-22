import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

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

        painter.drawLine(QtCore.QPoint(10, 10), QtCore.QPoint(100, 100))
        painter.end()



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
