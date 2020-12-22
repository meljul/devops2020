#!/usr/bin/python3
import sqlite3
import os

db_path = 'meals.db' ###Variable globale



def connect_to_db(db_path):
    db_link = None
    try:
        db_link = sqlite3.connect(db_path)
    except sqlite3.Error as error:
        print("Error while connecting to SQLite on path : ", error)
    return db_link

db_link = connect_to_db('meals.db')

db_cursor = db_link.cursor()
