__author__ = 'Alex'
import sqlite3
class AddRow():
    def __init__(self):
        pass

    # row method that takes in parameters and adds them to the query
    def row(self, cursor, connection, id, prodID, prodName, qnt, price, desc):
        # sets variables to be inserted
        rowID = id
        productID = prodID
        name = prodName
        quantity = qnt
        prodPrice = price
        description = desc

        try:
        # calls the connection cursor to insert data into the database
            cursor.execute("INSERT INTO PRODUCTS(RowID, ProductID, ProductName, InsertTime, Quantity, Price, Description)\
                        VALUES ("+str(rowID)+", "+str(productID)+", '"+name+"',(CURRENT_TIMESTAMP),"
                                 +str(quantity)+", "+str(prodPrice)+", '"+description+"')")

            # commits the changes
            # prints success statement
            connection.commit()
            print("--------------------------")
            print("Row Added Successfully!")
            print()

        #prints Error if and error occurs
        except sqlite3.IntegrityError:
            print("---------------------------------------")
            print("ERROR! RowID already exists in Column!")
            print()