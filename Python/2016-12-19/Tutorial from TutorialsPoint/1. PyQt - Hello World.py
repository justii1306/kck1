import sys
from PyQt4 import QtGui

def window():
    app = QtGui.QApplication(sys.argv)      # Uruchomienie aplikacji PyQt
    w = QtGui.QWidget()                     # Okno PyQt
    b = QtGui.QLabel(w)                     # Pole tekstowe wewnątrz okna
    b.setText("Hello, World")               # Ustawienie tekstu wewnątrz okna PyQt
    w.setGeometry(100,100,200,50)           # Ustawienie okna (pierwsze 2 - początek okna, kolejne dwa - szerokość i wysokość)
    b.move(50,20)                           # Przesunięcie względem lewego górnego rogu
    w.setWindowTitle("Hello, World")        # Ustawienie tytułu okna
    w.show()                                # Wyświetlenie okna
    sys.exit(app.exec_())

if __name__ == '__main__':                  # ?
    window()
