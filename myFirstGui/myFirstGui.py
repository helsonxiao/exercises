import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("myFirstGui.ui")[0]


class myWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x,y)

app = QtGui.QApplication(sys.argv)
myWindow = myWindowClass()
myWindow.show()
app.exec_()