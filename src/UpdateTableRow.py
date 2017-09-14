__author__ = 'Alex'
import sqlite3
class UpdateRow():
    def __init__(self):
        pass

    # updates a row via rowid
    def row(self, cursor, connection, column, nInput, id):
        try:
            cursor.execute("UPDATE Products SET " + str(column) + "=('" + str(nInput) + "') WHERE RowID=" + str(id) + ";")

            # if successful, print these statements and commit
            print("----------------")
            print("Update Success!")
            print()
            # commits changes to database
            connection.commit()

        #if unsuccessful, catch error and print these statements
        except sqlite3.OperationalError:
            print("------------------------------------------------------------------------")
            print("Incorrect Input! Please check that your column name and ID is correct!")
            print()