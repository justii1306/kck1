def initUI(self):
self.btn = QtGui.QPushButton('Dialog', self)
self.btn.move(20, 20)
self.btn.clicked.connect(self.showDialog)
self.le = QtGui.QLineEdit(self)
self.le.move(130, 22)
self.setGeometry(300, 300, 290, 150)
self.setWindowTitle('Input dialog')
self.show()
def showDialog(self):
text,ok=QtGui.QInputDialog.getText(self,'Dialog', 'podaj tekst:')
if ok: self.le.setText(str(text))