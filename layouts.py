from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # widget = Color("red")
        # self.setCentralWidget(widget)

        v_layout = QVBoxLayout()
        v_layout.addWidget(Color("red"))
        v_layout.addWidget(Color("green"))
        v_layout.addWidget(Color("blue"))

        h_layout = QHBoxLayout()
        h_layout.addWidget(Color("red"))
        h_layout.addWidget(Color("green"))
        h_layout.addWidget(Color("blue"))

        main_layout = QHBoxLayout()

        g_layout = QGridLayout()
        g_layout.addWidget(Color("red"), 0, 0)
        # g_layout.addWidget(Color("green"), 0, 1)
        g_layout.addWidget(Color("blue"), 1, 0)
        g_layout.addWidget(Color("yellow"), 1, 1)

        # s_layout = QStackedLayout()
        # s_layout.addWidget(Color("red"))
        # s_layout.addWidget(Color("green"))
        # s_layout.addWidget(Color("blue"))
        # s_layout.setCurrentIndex(2)

        main_layout.addLayout(v_layout)
        main_layout.addLayout(h_layout)
        main_layout.addLayout(g_layout)
        # main_layout.addLayout(s_layout)
        # main_layout.setContentsMargins(0, 0, 0, 0)
        # main_layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        # pagelayout = QVBoxLayout()
        # button_layout = QHBoxLayout()
        # layout = QStackedLayout()
        # pagelayout.addLayout(button_layout)
        # pagelayout.addLayout(layout)
        # for n, color in enumerate(['red','green','blue','yellow']):
        #     btn = QPushButton( str(color) )
        #     btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n) )
        #     button_layout.addWidget(btn)
        #     layout.addWidget(Color(color))
        # widget = QWidget()
        # widget.setLayout(pagelayout)
        # self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()