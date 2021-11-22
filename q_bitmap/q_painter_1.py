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
        pen.setWidth(40)
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)

        # Draw Line
        # painter.drawLine(10, 10, 300, 200)

        # Draw Point
        
        painter.drawPoint(200, 200)
        
        painter.end()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
