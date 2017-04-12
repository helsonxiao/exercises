import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("myFirstGui.ui")[0]


class myWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
myWindow = myWindowClass()
myWindow.show()
app.exec_()