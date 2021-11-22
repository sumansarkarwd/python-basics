import sys
from PyQt5 import QtWidgets, uic

def mainwindow_setup(mainwindow):
    mainwindow.setWindowTitle("From UI File")

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
mainwindow_setup(window)
window.show()

app.exec_()
