import enquiries
import os
import datetime
import shutil
import sys

from my_sqlite3 import *

##########################
#### Global variables ####
##########################
db_name = 'meals.db'
db_path = db_name #will be different if "db" is not in the same directory

def add_employee(first_name,family_name,email_address):

    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "INSERT INTO employee(first_name,family_name,email_address) VALUES (?,?,?)"
    sql_values = (first_name,family_name,email_address)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)

def get_employee(id):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)

    sql_query = "SELECT first_name,family_name,email_address,id FROM employee WHERE id=?"
    sql_values = (id,)
    query_result = read_from_cursor(db_cursor,sql_query,sql_values) # [('Jack', 'DAVIS', None)]
    db_cursor.close()
    disconnect_from_db(db_link)
    return query_result


def modify_employee(user_id,user_name,user_surname,user_email):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)

    sql_query = "UPDATE employee SET first_name = ?, family_name = ?, email_address = ? WHERE id=?"
    sql_values = (user_name,user_surname,user_email,user_id)

    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)


def add_menu(menu_desc,menu_price):

    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "INSERT INTO menu(description, price) VALUES (?,?)"
    sql_values = (menu_desc,menu_price)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)

def get_menu(id):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)

    sql_query = "SELECT description, price FROM menu WHERE id=?"
    sql_values = (id,)
    query_result = read_from_cursor(db_cursor,sql_query,sql_values)
    db_cursor.close()
    disconnect_from_db(db_link)
    return query_result


def modify_menu(menu_id,menu_desc,menu_price):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)

    sql_query = "UPDATE menu SET description = ?, price = ? WHERE id=?"
    sql_values = (menu_desc,menu_price,menu_id)

    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)

def get_menu_price(menu_id):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "SELECT price FROM menu WHERE id=?"
    sql_values = (menu_id,)
    query_result = read_from_cursor(db_cursor,sql_query,sql_values)
    menu_price = query_result[0][0]
    disconnect_from_db(db_link)
    return menu_price

def add_purchase(purchase_date, employee_id):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "INSERT INTO purchase(date,employee_id) VALUES (?,?)"
    sql_values = (purchase_date,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)

    disconnect_from_db(db_link)

def add_purchase_detail(purchase_id,menu_id,menu_price):
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "INSERT INTO purchase_detail(purchase_id,menu_id,menu_price) VALUES (?,?,?)"
    sql_values = (purchase_id,menu_id,menu_price)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)


def get_purchase_id():
    db_link = connect_to_db(db_path)
    db_cursor = create_cursor(db_link)
    sql_query = "SELECT MAX(id) FROM purchase"
    query_result = read_from_cursor(db_cursor,sql_query)
    disconnect_from_db(db_link)
    if query_result[0][0] != None:
        last_purchase_id = query_result[0][0]
    else:
        last_purchase_id = 0
    purchase_id = last_purchase_id + 1
    return purchase_id
