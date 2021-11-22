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
        pen.setColor(Qt.red)
        pen.setWidth(5)
        painter.setPen(pen)

        painter.drawPoint(10, 10)

        pen.setColor(Qt.blue)
        pen.setWidth(10)
        painter.setPen(pen) # important to set the pen again after changing config
        painter.drawPoint(50, 50)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
