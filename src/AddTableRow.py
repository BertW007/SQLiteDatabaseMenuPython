__author__ = 'Alex'
import sqlite3
class AddRow():
    def __init__(self):
        pass

    def row(self, cursor, id, prodName, qnt, price, desc):
        cursor.execute("INSERT")