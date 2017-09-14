__author__ = 'Alex'
import sqlite3

class DisplayRows():
    def __init__(self):
        pass

    def allRows(self, connection):
        # displays all rows in the Products Table
        cursor = connection.execute("SELECT RowID, ProductID, ProductName, InsertTime, Quantity, Price, Description\
                                    FROM Products")

        # somewhat neat print for displaying table rows
        print("RowID\t\tProductID\t\t\tProductName\t\t\t\tInsertTime\t\t\t\t\t\t\tQuantity\t\t   Price\t\t\tDescription")
        print("--------------------------------------------------------------------------------------------------------"
              "----------------------------------------------------")

        # loop that will print all rows in the table
        for row in cursor:

            print("RowID = ", str(row[0])+" | "+" ProductID = ", str(row[1])+" | "+" ProductName = ", str(row[2])+" | "+" InsertTime = ", str(row[3])
                +" | "+" Quantity = ", str(row[4])+" | "+" Price = ", str(row[5])+" | "+" Description = ", str(row[6]))

        print()


    def singleRow(self, connection, id):
        # displays one row in the Products Table based on input via RowID
        cursor = connection.execute("SELECT RowID, ProductID, ProductName, InsertTime, Quantity, Price, Description\
                                    FROM Products WHERE RowID =" +str(id)+";")

        # loop that will print a single row in the table based on input via RowID
        print()
        # prints selected row
        for row in cursor:
            print("RowID = ", str(row[0])+" | "+" ProductID = ", str(row[1])+" | "+" ProductName = ", str(row[2])+" | "+" InsertTime = ", str(row[3])
                +" | "+" Quantity = ", str(row[4])+" | "+" Price = ", str(row[5])+" | "+" Description = ", str(row[6]))

        print()
