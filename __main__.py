__author__ = 'Alex'
import sqlite3
from src.CreateDatabaseTable import Create
from src.UI import UI
def main():
    # gets instance for Classes
    decision = UI
    # sets variable databaseName = a users input for a filename
    decision.Interface(decision)

if __name__ == '__main__':
    main()