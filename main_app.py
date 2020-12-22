# -- coding: utf-8 --
#Lib utilisées : fpdf, pyqt
import sys
from UI.w_main import *
from UI.w_add_user import *
from UI.w_edit_user import *
from UI.w_add_menu import *
from UI.w_edit_menu import *
from UI.w_get_id import *
import gest_pdf
import data
from purchase import *


current_menu = ""

####################################
# Gestion des fenêtres             #
####################################
def open_w_add_user():
    c_w_add_user = w_add_user()
    c_w_add_user.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    c_w_add_user.exec_()

def open_w_edit_user():
    to_edit = open_w_get_id()
    to_edit = int(to_edit)
    if to_edit >= 0:
        c_w_edit_user = w_edit_user(to_edit)
        c_w_edit_user.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        c_w_edit_user.exec_()

def open_w_add_menu():
    c_w_add_menu = w_add_menu()
    c_w_add_menu.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    c_w_add_menu.exec_()

def open_w_edit_menu():
    to_edit = open_w_get_id()
    to_edit = int(to_edit)
    if to_edit >= 0:
        c_w_edit_menu = w_edit_menu(to_edit)
        c_w_edit_menu.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        c_w_edit_menu.exec_()

def open_w_get_id():
    c_w_get_id = w_get_id()
    if c_w_get_id.exec_() == QtWidgets.QDialog.Accepted:
        return int(c_w_get_id.le_id.text())
    else:
        return -1

def open_w_select_user():
    to_select = open_w_get_id()
    to_select = int(to_select)
    global current_purchase
    if to_select >= 0:
        to_return = get_user(to_select)
        current_purchase = purchase(to_select)
        current_user = to_select


    else:
        to_return = -1
    return to_return


####################################
# Gestion purchase                 #
####################################
def add_entry_to_purchase():
    global current_purchase
    global current_menu
    cur_pur = current_purchase
    cur_pur.add_menu_to_purchase(current_menu)
    current_menu = ""
    return refresh_purchase_text()

def remove_entry_to_purchase():
    global current_purchase
    global current_menu
    if current_menu == "":
        cur_pur = current_purchase
        cur_pur.remove_last_menu_added()
    else :
        current_menu = ""
    return refresh_purchase_text()

def refresh_purchase_text():
    global current_purchase
    cur_pur = current_purchase
    return cur_pur.get_formated_ticket()

def add_char_current_menu(char):
    global current_menu

    if current_menu != "" or char != "0":
        current_menu += char

    return current_menu

def validate_purchase():
    global current_purchase
    cur_pur = current_purchase

    cur_pur.save_purchase_purchase_details()
    gest_pdf.createPDF(cur_pur)
    return 0






####################################
# Gestion accès modèle             #
####################################
def add_user(user_name,user_surname,user_email):
     data.add_employee(user_name,user_surname,user_email)

def edit_user(user_id,user_name,user_surname,user_email):
    data.modify_employee(user_id,user_name,user_surname,user_email)

def get_user(user_id):
    user_values = data.get_employee(user_id)
    return user_values


def add_menu(menu_desc,menu_price):
     data.add_menu(menu_desc,menu_price)

def edit_menu(menu_id,menu_desc,menu_price):
    data.modify_menu(menu_id,menu_desc,menu_price)

def get_menu(menu_id):
    menu_values = data.get_menu(menu_id)
    return menu_values

def get_menu_price(menu_id):
    menu_price = data.get_menu_price(menu_id)
    return menu_price


def add_purchase(purchase_date, employee_id):
    data.add_purchase(purchase_date, employee_id)

def add_purchase_detail(purchase_id,menu_id,menu_price):
    data.add_purchase_detail(purchase_id, menu_id, menu_price)

def get_next_purchase_id():
    next_purchase_id = data.get_purchase_id()
    return next_purchase_id




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)


    current_purchase = -1
    w_main = w_main()
    w_main.show()


    #app.exec()

    sys.exit(app.exec_())
