__author__ = 'Alex'
import sqlite3

class Create():
    def __init__(self):
        pass

    # takes an input from person for the sqlite file
    def Create_Database(self):
        sqlFile = str(input("Please enter in the Name of a database or the Name of a new database: "))
        return sqlFile

    # gets connection to the database via file
    def Connect(self, file):
        conn = sqlite3.connect(file)
        print('Connection to "' + file + '" success!')

        return conn

    # gets the cursor via connection
    def get_cursor(self, connection):
        cursor = connection.cursor()

        return cursor

    # creates Products table via cursor
    def Create_Table(self, cursor):
        try:
            cursor.execute('CREATE TABLE Products'
                       '(RowID INT PRIMARY KEY NOT NULL,'
                       'ProductID INT NOT NULL,'
                       'ProductName TEXT NOT NULL,'
                       'InsertTime TEXT NULL,'
                       'Quantity INT NOT NULL,'
                       'Price REAL NOT NULL,'
                       'Description CHAR(50) NOT NULL);')

            print("------------------------------------")
            return print("Products Table Created Successfully!")

        # catches an error if the table is already in the database
        except(sqlite3.OperationalError):
            print("-----------------------")
            return print("Table already exists!")