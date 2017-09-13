__author__ = 'Alex'
from src.CreateDatabaseTable import Create
class UI:
    def __init__(self):
        pass

    def Interface(self):
        database = Create
        UI.Options(UI)
        userOption = int(input("Which option would you like to select? "))

        if userOption == 1:
            print("-----OPTION 1-----\n")
            file = database.Create_Database(database)
            database.Connect(database, file)


    def Options(self):
        option1 = "1): Create a new Database and Database Table"
        option2 = "2): Add a row of data to Table"
        option3 = "3): Update a row of data"
        option4 = "4): Delete a row of data"
        option5 = "5): Display all rows"
        option6 = "6): Display a single row of data"

        print("OPTIONS:\n"
              ,option1+"\n"
              ,option2+"\n"
              ,option3+"\n"
              ,option4+"\n"
              ,option5+"\n"
              ,option6+"\n")
