# Zmiana nazwy okna dialogowego

from PyQt4 import QtGui


class WindowTitleDialog(QtGui.QInputDialog):
    @staticmethod
    def changeWindowTitle(window: QtGui.QMainWindow):
        text, ok = WindowTitleDialog.getText(window, 'Zmiana tytułu okna', 'Podaj nowy tytuł okna:')
        if ok: window.setWindowTitle(text)
