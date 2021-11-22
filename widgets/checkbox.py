from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        checkboxWidget = QCheckBox("Hello")
        checkboxWidget.setChecked(True)
        checkboxWidget.stateChanged.connect(self.checkboxStateChangedHandler)
        self.setCentralWidget(checkboxWidget)

    def checkboxStateChangedHandler(self, state):
        if state == Qt.Checked:
            print("Checked")
        else:
            print("Unchecked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()