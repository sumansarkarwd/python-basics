from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        comboBox = QComboBox()
        comboBox.addItems(["Messi", "Dibala"])
        comboBox.currentIndexChanged.connect( self.indexChanged )
        comboBox.currentIndexChanged[str].connect( self.text_changed )

        self.setCentralWidget(comboBox)
    
    def indexChanged(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()