#! python2
# coding:utf-8

import sys
from PyQt4 import QtGui, QtCore, uic

form_class = uic.loadUiType("GuessGame.ui")[0]


class myWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.lb2.setText("You have 3 times to guess an integer number between 1 and 10.")
        self.guessBtn.clicked.connect(self.guessBtn_clicked)
        self.tries = 0
        self.secret = 7

    def guessBtn_clicked(self):
        num = int(self.numEdit.text())
        if self.tries < 3:
            if  num < self.secret:
                self.lb2.setText("Too small!")
            elif num > self.secret:
                self.lb2.setText("Too big!")
            elif num == self.secret:
                self.lb2.setText("Good job!")
        else:
            self.lb2.setText("You have no chances to guess.")
        self.tries += 1

app = QtGui.QApplication(sys.argv)
myWindow = myWindowClass()
myWindow.show()
app.exec_()