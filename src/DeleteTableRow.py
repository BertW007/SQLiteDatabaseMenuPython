__author__ = 'Alex'
import sqlite3

class DeleteRow():
    def __init__(self):
        pass

    def row(self, cursor, connection, id):
        try:
            # tries to delete a row from the products table via the RowID
            cursor.execute("DELETE FROM Products WHERE RowID = " +str(id)+";")

            # prints success statement and commits changes to database
            print("---------------------------------------")
            print("Success! Deleted Row #" + str(id)+ ".")
            print()
            connection.commit()

        except sqlite3.OperationalError:
            print("Error! Incorrect RowID!")