import sys
import sqlite3
from PyQt5 import QtWidgets

db = sqlite3.connect("hospital.db")
cursor = db.cursor()
db.commit()

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
