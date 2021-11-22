import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QPoint, QRect, Qt

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
        pen.setWidth(2) # The width of the pen has no effect on the appearance of the text
        painter.setPen(pen)

        font = QtGui.QFont("Times")
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, "Hello World")

        painter.drawRect(100, 100, 100, 100) # this is to show clip border
        # specifying position, width and height can clip the text
        # rest of the area will be hidden
        painter.drawText(100, 100, 100, 100, Qt.AlignHCenter, 'Hello, world!')

        painter.end()



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
