import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        #Create connection
        self.conn = sqlite3.connect('fati.db')

    def create_table(self, name, values):

        #Declare cursor with connection maked
        try:
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE " + name + "(id integer PRIMARY KEY, " + values + ")")
            self.conn.commit()
        except Error: 
            print(Error)

    def insert(self, table, data):
        try:
            elements = ""
            values = ""
            for item in data:
                elements = (elements + "," if elements != "" else "") + str(item)
                values = ("'" + values + "'," if values != "" else "") + str(data.get(item))

            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO " + table + " (" + elements + ") VALUES (" + values + ")")

            self.conn.commit()
        except Error:
            print(Error)

    def get(self, table):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM " + table)

            rows = cursor.fetchall()

            return rows
        except Error:
            print(Error)


    def view_tables(self):
        cursor = self.conn.cursor()
        cursor. execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor. fetchall())

