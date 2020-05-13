import sys
import sqlite3
from design import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage,QPixmap

db = sqlite3.connect("hospitaltest.db")
cursor = db.cursor()
db.commit()

# convert to binary for photo
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.loadphoto.clicked.connect(self.uploadphoto)
        self.ui.pushButton_3.clicked.connect(self.testdownload)
        self.ui.clearbutton.clicked.connect(self.clear)
        global defpixmap
        defpixmap = QPixmap('default.jpg')
        defpixmap = defpixmap.scaled(241, 211)
        self.ui.photoLabel.setPixmap(defpixmap)

    #upload photo function
    def uploadphoto(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose image','c:\\', "Image files (*.jpg *.gif *.png)")
        if not fname[0]:
            None
        else:
            imagePath = fname[0]
            pixmap = QPixmap(imagePath)
            pixmap = pixmap.scaled(241, 211)
            global tmpfileway
            tmpfileway = fname[0]
            self.ui.photoLabel.setPixmap(pixmap)


#add info in DB
    def add(self):
        name = self.ui.lineEditname.text()
        surname = self.ui.linesurname.text()
        age = self.ui.lineage.text()
        birth = self.ui.linebirth.text()
        address = self.ui.lineadress.text()
        phone = self.ui.linephone.text()
        chamber = self.ui.linechamber.text()
        datein = self.ui.dateEdit.text()
        dateout = self.ui.dateEdit_2.text()
        empPhoto = convertToBinaryData(tmpfileway)
        cursor.execute("""INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (None, name, surname, age, birth, address, phone, chamber, datein, dateout, empPhoto))
        db.commit()
        cursor.close()

    def testdownload(self):
        nametmp = self.ui.lineEdit.text()
        cursor.execute("""SELECT patientid, patientphoto FROM patients WHERE patientid = ? """, nametmp)

        record = cursor.fetchall()
        for row in record:
            idtmp = row[0]
            photo = row[1]
        photoPath = "D:\Desktop\hospitalqt\\" + str(idtmp) + ".jpg"
        writeTofile(photo, photoPath)

    def clear(self):
        self.ui.lineEditname.setText(None)
        self.ui.linesurname.setText(None)
        self.ui.lineage.setText(None)
        self.ui.linebirth.setText(None)
        self.ui.lineadress.setText(None)
        self.ui.linephone.setText(None)
        self.ui.linechamber.setText(None)
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.photoLabel.setPixmap(defpixmap)

app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec_()
