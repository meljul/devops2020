import main_app
import datetime

class purchase():

    def __init__(self,user_id):
        self.purchase_details = []
        self.current_date = datetime.datetime.now()
        self.formated_date = self.current_date.strftime("%d-%m-%Y %H:%M:%S")
        self.purchase_id = main_app.get_next_purchase_id()
        self.total = 0

        employee_datas = main_app.get_user(user_id)
        self.employee_name ="{} {}".format(employee_datas[0][0],employee_datas[0][1])
        self.employee_id = employee_datas[0][3]

    def get_formated_ticket(self):
        formated_ticket = "Commande n° {}\n".format(self.purchase_id)
        formated_ticket += "Date : {}\n".format(self.formated_date)
        formated_ticket += "Nom : {}\n".format(self.employee_name)
        total = 0
        if len(self.purchase_details) > 0:
            for x in self.purchase_details:
                formated_ticket += "Menu : {} {} \n".format(x[1],x[2])
                total += x[2]
                total = round(total,2)
                self.total = total
            formated_ticket += "TOTAL : {}".format(total)
        return formated_ticket

    def add_menu_to_purchase(self, _menu_id):
        menu_datas = main_app.get_menu(_menu_id)
        menu_id = _menu_id
        menu_desc = menu_datas[0][0]
        menu_price = menu_datas[0][1]


        purchase_detail = [menu_id,menu_desc,menu_price]
        self.purchase_details.append(purchase_detail)

    def remove_last_menu_added(self):
        self.purchase_details.pop()

    def save_purchase_purchase_details(self):
        if len(self.purchase_details) > 0:
            purchase_date = self.current_date
            employee_id = self.employee_id
            main_app.add_purchase(purchase_date, employee_id)
            for x in self.purchase_details:
                _purchase_id = self.purchase_id
                _menu_id = x[0]
                _menu_price = x[2]

                main_app.add_purchase_detail(_purchase_id, _menu_id, _menu_price)

        #self.purchase_details = []
