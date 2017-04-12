import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("tempconv.ui")[0]


class myWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.buttonC2F.clicked.connect(self.buttonC2F_clicked)
        self.buttonF2C.clicked.connect(self.buttonF2C_clicked)
        self.actionC_to_F.triggered.connect(self.buttonC2F.clicked)
        self.actionF_to_C.triggered.connect(self.buttonF2C_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
    def buttonC2F_clicked(self):
        print("success")
        cel = float(self.editCel.text())
        fahr = cel * 9.0 / 5 + 32
        self.spinFahr.setValue(int(fahr + 0.5))


    def buttonF2C_clicked(self):
        print("success")
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5.0 / 9
        cel_text = '%.2f' % cel
        self.editCel.setText(cel_text)

    def menuExit_selected(self):
        self.close()
app = QtGui.QApplication(sys.argv)
myWindow = myWindowClass(None)
myWindow.show()
app.exec_()