from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()
        # widgets = [
        #     QCheckBox, 
        #     QComboBox, 
        #     QDateEdit, 
        #     QDateTimeEdit, 
        #     QDial, 
        #     QDoubleSpinBox, 
        #     QFontComboBox, 
        #     QLCDNumber, 
        #     QLabel, 
        #     QLineEdit, 
        #     QProgressBar, 
        #     QPushButton, 
        #     QRadioButton, 
        #     QSlider, 
        #     QSpinBox, 
        #     QTimeEdit, 
        #     QToolButton
        # ]
        # for w in widgets:
        #     layout.addWidget(w())

        widget = QLabel("Qt is: ")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget)

        checkboxWidget = QCheckBox("Hello")
        checkboxWidget.setChecked(True)
        checkboxWidget.stateChanged.connect(self.checkboxStateChangedHandler)
        layout.addWidget(checkboxWidget)

    def checkboxStateChangedHandler(self, state):
        print(state)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()