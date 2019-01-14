# Ustaw kolor tła
from PyQt4 import QtCore

from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class ColorChanger(QtGui.QDialog):

    def __init__(self, parent: QtGui.QMainWindow):
        super(ColorChanger, self).__init__();

        self.oldColor=parent.palette()
        self.mainWindow = parent

        self.__initUI__()

    def __initUI__(self):
        grid = self.__createSliders__()

        # rect = QtGui.QLabel()
        # rect.setPalette(palette)
        # # rect.setStyleSheet("background-color: green")
        # rect.setFixedSize(50, 100)

        # hbox = QtGui.QHBoxLayout()
        # hbox.addLayout(grid)
        # hbox.addWidget(rect)

        # Utworzenie przycisków
        buttons = self.__createWindowButtons()

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(buttons)

        self.setLayout(vbox)
        self.setWindowTitle("Zmiana koloru okna")

    def __createWindowButtons(self):
        okB = QtGui.QPushButton('OK', self)
        okB.clicked.connect(self.close)
        anB = QtGui.QPushButton('Anuluj', self)
        anB.clicked.connect(self.__cancel__)

        buttons = QtGui.QHBoxLayout()
        buttons.addWidget(okB)
        buttons.addWidget(anB)
        return buttons

    def __createSliders__(self):
        elements = [QtGui.QLabel('Czerwony', self),
                    self.__createQSlider__(0),
                    QtGui.QLabel('Zielony', self),
                    self.__createQSlider__(1),
                    QtGui.QLabel('Niebieski', self),
                    self.__createQSlider__(2)]
        pos = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        grid = QtGui.QGridLayout()
        for i in range(len(elements)):
            grid.addWidget(elements[i], pos[i][0], pos[i][1])

        return grid

    def __createQSlider__(self, rgbNum):
        slider = QtGui.QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(255)
        # slider.setValue(self.oldColor.)
        return slider

    def __cancel__(self):
        self.mainWindow.setPalette(self.oldColor)
        self.close()

    def __changeColor(self):
        None

    @staticmethod
    def changeColor(parrent: QtGui.QMainWindow):
        ColorChanger(parrent).exec_()
