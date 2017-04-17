#! python2
# coding:utf-8
import random, sys
from PyQt4 import QtGui, uic

form_class = uic.loadUiType('hangman.ui')[0]


def find_letter(letter, a_string):
    locations = []
    start = 0
    # 当index = -1 时，代表此时的start之后不再有letter出现
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations


def replace_letter(letter, locations, string):
    new_string = ''
    for i in range(0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string


def dashed(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    dashes = ''
    for i in word:
        if i in letters:
            dashes = dashes + "-"
        else:
            dashes = dashes + i
    return dashes


class MyWeight(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.menuExit_selected)
        self.guessButton.clicked.connect(self.guessButton_clicked)
        self.pieces = [self.head, self.body, self.leftArm, self.leftLeg,  # Parts of the man
                       self.rightArm, self.rightLeg]
        self.gallows = [self.ground, self.gallow, self.gallow_2, self.gallow_3]
        self.pieces_shown = 0
        self.currentWord = ''

        # get the word list
        f = open('words.txt', 'r')
        self.lines = f.readlines()
        f.close()
        self.newGame()

    def newGame(self):
        for i in self.pieces:
            i.setFrameShadow(QtGui.QFrame.Plain)
            i.setHidden(True)
        for i in self.gallows:
            i.setFrameShadow(QtGui.QFrame.Plain)

        self.previous.setText('')
        self.currentWord = random.choice(self.lines)
        self.currentWord = self.currentWord.strip()
        self.word.setText(dashed(self.currentWord))
        self.pieces_shown = 0

    def menuExit_selected(self):
        self.close()

    def guessButton_clicked(self):
        guess = str(self.guessBox.text())
        if str(self.previous.text()) != "":
            self.previous.setText(str(self.previous.text()) + ", " + guess)
        else:
            self.previous.setText(guess)

        # guess a letter
        if len(guess) == 1:
            if guess in self.currentWord:
                locations = find_letter(guess, self.currentWord)
                self.word.setText(replace_letter(guess,locations,self.word.text()))
                if self.word.text() == self.currentWord:
                    self.win()
            else:
                self.wrong()
        # guess a word
        else:
            if guess == self.currentWord:
                self.win()
            else:
                self.wrong()
        self.guessBox.setText("")

    def win(self):
        QtGui.QMessageBox.information(self, "hangman", "You win!")
        self.newGame()

    def wrong(self):
        self.pieces_shown += 1
        for i in range(self.pieces_shown):
            self.pieces[i].setHidden(False)
        if self.pieces_shown == len(self.pieces):
            message = "You lose. The word was " + self.currentWord
            QtGui.QMessageBox.warning(self, "hangman", message)
            self.newGame()

app = QtGui.QApplication(sys.argv)
myapp = MyWeight(None)
myapp.show()
app.exec_()