#!/usr/bin/python3
import sqlite3

def connect_to_db(db_path):
    db_link = None
    try:
        db_link = sqlite3.connect(db_path)
    except sqlite3.Error as error:
        print("Error while connecting to SQLite on path : ", error)
    return db_link

db_link = connect_to_db('meals.db')

db_cursor = db_link.cursor()

data = input('Enter your family name : ')
print(data)

db_cursor.execute("SELECT * FROM employee WHERE family_name = ?", (data,))

result = db_cursor.fetchall()
print(result)

print(result)
