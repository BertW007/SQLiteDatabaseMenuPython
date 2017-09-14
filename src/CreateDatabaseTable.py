__author__ = 'Alex'
import sqlite3

class Create():
    def __init__(self):
        pass

    def Create_Database(self):
        sqlFile = str(input("Please enter in the Name of a database or the Name of a new database: "))
        return sqlFile

    def Connect(self, file):
        conn = sqlite3.connect(file)
        conn.cursor()
        print('Connection to "' + file + '" success!')

        return conn

    def Create_Table(self, cursor):
        try:
            cursor.execute('CREATE TABLE Products'
                       '(ProductID INT PRIMARY KEY NOT NULL,'
                       'ProductName TEXT NOT NULL,'
                       'InsertTime TEXT NULL,'
                       'Quantity INT NOT NULL,'
                       'Price REAL NOT NULL,'
                       'Description CHAR(50) NOT NULL);')
            return print("Products Table Created Successfully!")

        except(sqlite3.OperationalError):
            return print("Table already exists!")