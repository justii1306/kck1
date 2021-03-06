def initUI(self):
self.textEdit = QtGui.QTextEdit()
self.setCentralWidget(self.textEdit)
self.statusBar()
akcja = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
akcja.setShortcut('Ctrl+O')
akcja.setStatusTip('Open new File')
akcja.triggered.connect(self.showDialog)
menubar = self.menuBar()
fileMenu = menubar.addMenu('&File')
fileMenu.addAction(akcja)
self.setGeometry(300, 300, 350, 300)
self.setWindowTitle('File dialog')
self.show()
def showDialog(self):
fn=QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:')
f = open(fn, 'r')
with f:
data = f.read()
self.textEdit.setText(data)