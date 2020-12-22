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

###################
#### Functions ####
###################
def choose_enquiry(): # choisir une requête
  os.system('clear') #cls sous windows
  options = ['Purchase',
    'Add employee',
    'Modify employee',
    'Add menu',
    'Modify menu',
    'Exit']
  choice = enquiries.choose('Choose one of these options: ', options)
  trigger_enquiry(choice)

def trigger_enquiry(choice): # déclencher une requête
  if (choice == 'Purchase'):
    purchase()
  elif (choice == 'Add employee'):
    add_employee()
  elif (choice == 'Modify employee'):
    modify_employee()
  elif (choice == 'Add menu'):
    add_menu()
  elif (choice == 'Modify menu'):
    modify_menu()
  elif (choice == 'Exit'):
    exit_program()

def purchase():
  purchase_id = get_purchase_id()
  current_date = datetime.datetime.now()
  formated_date = current_date.strftime("%d-%m-%Y %H:%M:%S")

  employee_id = get_employee_id()
  employee_name = get_employee_name(employee_id)
  ticket_data = [purchase_id,formated_date,employee_name]

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO purchase(date,employee_id) VALUES (?,?)"
  sql_values = (formated_date,employee_id)
  write_to_cursor(db_cursor,sql_query,sql_values)

  menu_id_list = get_id_list('menu')

  while True:
    menu_id = input("\nEnter menu ID : ")

    if not menu_id: #TODO if menu_id in menu_id_list:
      break

    os.system('clear')
    menu_id = int(menu_id)
    if menu_id in menu_id_list:
        menu_price = get_menu_price(menu_id) #TODO get_purchase_detail plutôt que get_menu_price?
        sql_query = "INSERT INTO purchase_detail(purchase_id,menu_id,menu_price) VALUES (?,?,?)"
        sql_values = (purchase_id,menu_id,menu_price)
        write_to_cursor(db_cursor,sql_query,sql_values)
        ticket_data.append(sql_values)
    display_ticket(ticket_data)

  confirm = input("Confirm your order (y/n) : ")
  if ((confirm == 'y') and (len(ticket_data) >= 4)):
    commit_to_db(db_link)
    disconnect_from_db(db_link)
    save_database(db_path)
  choose_enquiry()

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

def get_employee_id(): #TODO idem que get_menu_id()?
  employee_id_list = get_id_list('employee')
  #print(employee_id_list) #[1, 2, 3, 4]
  employee_id = 0
  while employee_id not in employee_id_list:
    os.system('clear')
    employee_id = input("Enter the employee ID : ")
    if not employee_id:
      employee_id = 0
    else:
      employee_id = int(employee_id)
  return employee_id

def get_id_list(table_name):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  if (table_name == 'employee'): #TODO simlify with ?
    sql_query = "SELECT id FROM employee"
  elif (table_name == 'menu'):
    sql_query = "SELECT id FROM menu"
  query_result = read_from_cursor(db_cursor,sql_query)
  id_list = []
  for id in query_result:
    id_list.append(id[0])
  disconnect_from_db(db_link)
  return id_list

def get_employee_name(employee_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT first_name,family_name FROM employee WHERE id=?"
  sql_values = (employee_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  employee_name = query_result[0][0] + ' ' + query_result[0][1]
  disconnect_from_db(db_link)
  return employee_name

def get_menu_price(menu_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT price FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  menu_price = query_result[0][0]
  disconnect_from_db(db_link)
  return menu_price

def display_ticket(ticket_data):
  purchase_line = 'Purchase number : ' + str(ticket_data[0])
  date_line = 'Date : ' + ticket_data[1]
  employee_line = 'Employee : ' + ticket_data[2] + '\n'

  print(purchase_line)
  print(date_line)
  print(employee_line)

  amount = 0.0
  for index in range(3,len(ticket_data)): #[purchase_id,date,employee,(p_id,menu_id,price)]
    menu_id = ticket_data[index][1]
    description = get_menu_description(menu_id)
    price = ticket_data[index][2]
    detail_string = "Menu: {:<18} {:>6} €"
    detail_line = detail_string.format(description,price)
    print(detail_line)
    amount = amount + price #TODO pourquoi 3.3 * 3 donne 9.89999999?
  amount_line = '\nAmount : ' + str(amount) + ' €'
  print(amount_line)

def get_menu_description(menu_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT description FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  description = query_result[0][0]
  disconnect_from_db(db_link)
  return description

def save_database(db_name):
  backup_dir = 'backup'
  if not os.path.isdir(backup_dir):
    os.makedirs(backup_dir)
  date = datetime.datetime.now()
  hour = date.strftime("%H")
  source = db_name
  backup = backup_dir + '/' + db_name + '_' + hour
  shutil.copyfile(source, backup)

def add_employee(first_name,family_name,email_address):


  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO employee(first_name,family_name,email_address) VALUES (?,?,?)"
  sql_values = (first_name,family_name,email_address)
  write_to_cursor(db_cursor,sql_query,sql_values)
  commit_to_db(db_link)
  disconnect_from_db(db_link)


def modify_employee():
  employee_id = input("Enter the employee ID : ")
  employee_id = int(employee_id)

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT first_name,family_name,email_address FROM employee WHERE id=?"
  sql_values = (employee_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values) # [('Jack', 'DAVIS', None)]
  first_name = query_result[0][0]
  family_name = query_result[0][1]
  email_address = query_result[0][2]
  db_cursor.close()

  db_cursor = create_cursor(db_link)
  new_first_name = input("First name [" + first_name + "] : ")
  if new_first_name:
    sql_query = "UPDATE employee SET first_name = ? WHERE id=?"
    sql_values = (new_first_name,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  new_family_name = input("Family name [" + family_name + "] : ")
  if new_family_name:
    sql_query = "UPDATE employee SET family_name = ? WHERE id=?"
    sql_values = (new_family_name,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  new_email_address = input("Email address [" + str(email_address) + "] : ")
  if new_email_address:
    sql_query = "UPDATE employee SET email_address = ? WHERE id=?"
    sql_values = (new_email_address,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  confirm = input("Confirm your modifications (y/n) : ")
  if confirm == 'y':
    commit_to_db(db_link)
    disconnect_from_db(db_link)
  choose_enquiry()

def add_menu():
  description = input("Description : ")
  price = input("Price [ex: 3.5] : ")

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO menu(description,price) VALUES (?,?)"
  sql_values = (description,price)
  write_to_cursor(db_cursor,sql_query,sql_values)

  confirm = input("Confirm your request (y/n) : ")
  if (confirm == 'y'):
    commit_to_db(db_link)
    disconnect_from_db(db_link)
  choose_enquiry()

def modify_menu():
  menu_id = input("Enter menu ID : ")

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT description,price FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  description = query_result[0][0]
  price = query_result[0][1]
  db_cursor.close()

  db_cursor = create_cursor(db_link)
  new_description = input("Description [" + description + "] : ")
  if new_description:
    sql_query = "UPDATE menu SET description = ? WHERE id=?"
    sql_values = (new_description,menu_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  new_price = input("Price [" + str(price) + "] : ")
  if new_price:
    sql_query = "UPDATE menu SET price = ? WHERE id=?"
    sql_values = (new_price,menu_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  confirm = input("Confirm your modification (y/n) : ")
  if confirm == 'y':
    commit_to_db(db_link)
    disconnect_from_db(db_link)
  choose_enquiry()

def exit_program():
  sys.exit()
