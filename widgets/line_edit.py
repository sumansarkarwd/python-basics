from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text here")

        # widget.setReadOnly(True)

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)
    
    def return_pressed(self):
        print("Return pressed")
        self.centralWidget().setText("BOOM!!!")

    def selection_changed(self):
        print("Selection changed", self.centralWidget().selectedText())

    def text_changed(self, text):
        print("Text changed:", text)

    def text_edited(self, text):
        print("Text edited:", text)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()