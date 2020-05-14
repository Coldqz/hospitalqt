import sys
import sqlite3

from mainWindowDesign import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt

db = sqlite3.connect("hospitaltest.db")
cursor = db.cursor()
db.commit()

# convert from photo to binary
def convertToBinaryData(filename):

    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# convert from binary to photo
def writeTofile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#buttons init
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.loadphoto.clicked.connect(self.uploadphoto)
        self.ui.pushButton_3.clicked.connect(self.testdownload)
        self.ui.clearbutton.clicked.connect(self.clear)
        self.ui.updatebutton.clicked.connect(self.updateinfo)
        self.ui.searchbynumber.clicked.connect(self.searchbyid)
#default photo init
        global defpixmap
        defpixmap = QPixmap('default.jpg')
        defpixmap = defpixmap.scaled(241, 211)
        self.ui.photoLabel.setPixmap(defpixmap)
        self.ui.photoLabel_2.setPixmap(defpixmap)

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

#test method for download photo from bd to folder
    def testdownload(self):
        nametmp = self.ui.lineEdit.text()
        cursor.execute("""SELECT patientid, patientphoto FROM patients WHERE patientid = ? """, nametmp)

        record = cursor.fetchall()
        for row in record:
            idtmp = row[0]
            photo = row[1]
        photoPath = "D:\Desktop\hospitalqt\\" + str(idtmp) + ".jpg"
        writeTofile(photo, photoPath)

#method for clear all lineedit elements
    def clear(self):
        self.ui.lineEditname.clear()
        self.ui.linesurname.clear()
        self.ui.lineage.clear()
        self.ui.linebirth.clear()
        self.ui.lineadress.clear()
        self.ui.linephone.clear()
        self.ui.linechamber.clear()
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.photoLabel.setPixmap(defpixmap)

    def searchbyid(self):
        tmpid = self.ui.lineEditsearch.text()
        record = cursor.execute("""SELECT patientid, patientname, patientsurname, patientage, patientbirthdate, patientadress, patientphone, patientchamber, patientdatein, patientdateout FROM patients WHERE patientid = ?""", tmpid)
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def updateinfo(self):
        query = "SELECT patientid, patientname, patientsurname, patientage, patientbirthdate, patientadress, patientphone, patientchamber, patientdatein, patientdateout FROM patients"
        record = cursor.execute(query)
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()