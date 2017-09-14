__author__ = 'Alex'
from src.CreateDatabaseTable import Create
from src.AddTableRow import AddRow
class UI:
    def __init__(self):
        pass

    def Interface(self):
        # gets instance for the Create class
        database = Create
        add = AddRow

        # variable to get file connection
        file = database.Create_Database(database)
        cursor = database.Connect(database, file)
        userOption = 7

        while userOption != 0:
            UI.Options(UI)
            userOption = int(input("Which option would you like to select? "))

            if userOption == 1:
                print("-----OPTION 1-------------------------------------------\n")

                # gets connection to database
                database.Create_Table(database, cursor)

            if userOption == 2:
                print("-----OPTION 2-------------------------------------------\n")

                add.row(add, cursor)



    def Options(self):
        option1 = "1): Create a new Database and Database Table"
        option2 = "2): Add a row of data to Table"
        option3 = "3): Update a row of data"
        option4 = "4): Delete a row of data"
        option5 = "5): Display all rows"
        option6 = "6): Display a single row of data"
        option7 = "0): EXIT PROGRAM"

        print("OPTIONS:\n"
              ,option1+"\n"
              ,option2+"\n"
              ,option3+"\n"
              ,option4+"\n"
              ,option5+"\n"
              ,option6+"\n"
              ,option7+"\n")
