from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.windowTitleChanged.connect(lambda x: self.customHandler())
        self.windowTitleChanged.connect(lambda x: self.customHandler(x))
        self.windowTitleChanged.connect(lambda x: self.customHandler(x, 25))

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
    def onWindowTitleChange(self, s):
        print(s)

    def customHandler(self, s="", i=0):
        print(s, i)
    
    def contextMenuEvent(self, event):
        print("Context Menu Event")
        super(MainWindow, self).contextMenuEvent(event)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()