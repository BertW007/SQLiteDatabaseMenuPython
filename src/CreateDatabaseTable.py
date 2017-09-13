__author__ = 'Alex'
import sqlite3

class Create():
    def __init__(self):
        pass

    def Create_Database(self):
        sqlFile = str(input("Please enter in a Name for the database: "))
        return sqlFile

    def Connect(self, file):
        conn = sqlite3.connect(file)
        conn.cursor()
        print('Connection to "' + file + '" success!')

    def Create_Table(self):
        pass