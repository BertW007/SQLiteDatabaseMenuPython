__author__ = 'Alex'
import sqlite3
def main():
    # declares the sqlite file
    sqlite_file = "sqlite_file"

    # connects to sqlite with selected sqlite file
    connect = sqlite3.connect(sqlite_file)
    connect.cursor()


if __name__ == '__main__':
    main()