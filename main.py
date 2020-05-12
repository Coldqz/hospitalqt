import sys
import sqlite3
#test5
db = sqlite3.connect('hospital.db')
cursor = db.cursor()
db.commit()