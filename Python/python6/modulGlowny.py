# Okno główne

import sys
from PyQt4 import QtGui

import modul1
# import modul2
import modul3

class MainWindow(QtGui.QMainWindow):
    color = QtGui.QPalette()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.color.setColor(QtGui.QPalette.Background, QtGui.QColor(0, 255, 0))
        self.initUI()

    def initUI(self):
        actions = [self.__createAction__('&Nazwa okna głównego', 'Ctrl+N', '', self.__changeTitle__),
                   self.__createAction__('&Ustaw kolor tła', 'Ctrl+U', '', self.__setBgcolor__),
                   self.__createAction__('&Zmień ikonę', 'Ctrl+Z', '', self.__changeIcon__)]

        option = self.menuBar().addMenu('&Dialog')
        for a in actions:
            option.addAction(a)

        # Skonfigurowanie okna
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Dialogi')
        # self.setStyleSheet("MainWindow {background-color: %s}" color)
        self.setPalette(self.color)
        self.show()

    def __createAction__(self, name, shortcut, statusTip, action):
        option = QtGui.QAction(name, self)
        option.setShortcut(shortcut)
        option.setStatusTip(statusTip)
        option.triggered.connect(action)
        return option

    def __changeTitle__(self):
        modul1.WindowTitleDialog.changeWindowTitle(self)

    def __setBgcolor__(self):
        # print('Set BGColor')
        modul3.ColorChanger.changeColor(self)

    def __changeIcon__(self):
        print('Change Icon')


def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow();
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
