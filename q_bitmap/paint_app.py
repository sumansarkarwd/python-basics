import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QPoint, QRect, Qt

COLORS = [
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 500)
        pixmap.fill(QtGui.QColor("#ececec"))
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor(COLORS[0])

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.last_x is None:
            self.last_x = ev.x()
            self.last_y = ev.y()
            return

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(5)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, ev.x(), ev.y())
        painter.end()
        self.update()

        self.last_x, self.last_y = ev.x(), ev.y()

    def mouseReleaseEvent(self, e):
        self.last_x, self.last_y = None, None

class QPalletButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(20, 20)
        self.color = color
        self.setStyleSheet('background-color: %s' % color)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)

        l.addWidget(self.canvas)

        pallet = QtWidgets.QHBoxLayout()
        self.add_pallet_button(pallet)

        l.addLayout(pallet)

        self.setCentralWidget(w)

    def add_pallet_button(self, l):
        for c in COLORS:
            b = QPalletButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            l.addWidget(b)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
