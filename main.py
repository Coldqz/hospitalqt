import sys
import sqlite3
from design import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage,QPixmap

db = sqlite3.connect("hospitaltest.db")
cursor = db.cursor()
db.commit()



class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.loadphoto.clicked.connect(self.uploadphoto)
        pixmap = QPixmap('default.jpg')
        pixmap = pixmap.scaled(241, 211)
        self.ui.photoLabel.setPixmap(pixmap)


    def test(self):
        self.ui.lineEditname.setText("qweq")

    def uploadphoto(self):
        self.photoLabel.setPixmap()

    def add(self):
        name = self.ui.lineEditname.text()
        surname = self.ui.linesurname.text()
        age = self.ui.lineage.text()
        birth = self.ui.linebirth.text()
        adress = self.ui.lineadress.text()
        phone = self.ui.linephone.text()
        chamber = self.ui.linechamber.text()
        datein = self.ui.dateEdit.text()
        dateout = self.ui.dateEdit_2.text()
        cursor.execute("""INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?)""", (None, name, surname, age, birth, adress, phone, chamber, datein, dateout))
        db.commit()


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec_()
