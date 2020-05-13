import sys
import sqlite3
from design import Ui_MainWindow
from PyQt5 import QtWidgets

db = sqlite3.connect("hospital.db")
cursor = db.cursor()
db.commit()

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec_()
