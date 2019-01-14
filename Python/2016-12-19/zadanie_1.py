import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def newButton(parrent, text, x, y, func):
    button = QPushButton(parrent)
    button.setText(text)
    button.move(x, y)
    button.clicked.connect(func)
    

def window() :
    app = QApplication(sys.argv)
    win = QDialog()
    newButton(win, "1", 0, 0, null)
    newButton(win, "2", 30, 0, null)
    newButton(win, "3", 60, 0, null)
    newButton(win, "4", 0, 0, null)
    newButton(win, "5", 0, 0, null)
    newButton(win, "6", 0, 0, null)
    newButton(win, "7", 0, 0, null)
    newButton(win, "8", 0, 0, null)
    newButton(win, "9", 0, 0, null)
    newButton(win, "+", 0, 0, null)
    newButton(win, "0", 0, 0, null)
    newButton(win, "=", 0, 0, null)

if __name__ == '__main__':
    window()
