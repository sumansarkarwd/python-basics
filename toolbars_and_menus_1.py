from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

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
        buttonAction.setCheckable(True)
        toolbar.addAction(buttonAction)

        buttonAction2 = QAction(QIcon("menu.png"), "&Your button 2", self)
        buttonAction2.setStatusTip("This is your button")
        buttonAction2.triggered.connect(self.onMyToolBarButtonClick2)
        buttonAction2.setCheckable(True)
        toolbar.addAction(buttonAction2)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(buttonAction)
        fileMenu.addSeparator()
        subMenu = fileMenu.addMenu("Submenu")
        subMenu.addAction(buttonAction2)

    def onMyToolBarButtonClick(self, s):
        print("Clicked the button!", s)

    def onMyToolBarButtonClick2(self, s):
        print("Clicked the button 2!", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()