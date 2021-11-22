from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class CustomDialog(QDialog):
    def __init__(self):
        super(CustomDialog, self).__init__()
        self.setWindowTitle("Custom Dialog")

        qBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(qBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        toolbar = QToolBar("My Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(toolbar)

        buttonAction = QAction(QIcon("menu.png"), "&Your button", self)
        buttonAction.setStatusTip("This is your button")
        buttonAction.triggered.connect(self.onMyToolBarButtonClick)

        toolbar.addAction(buttonAction)

    def onMyToolBarButtonClick(self):
        print("You clicked the button!")

        dlg = CustomDialog()
        if dlg.exec_():
            print("Dialog accepted")
        else:
            print("Dialog rejected")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()