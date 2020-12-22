from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.Qt import Qt

import main_app


class w_main(QtWidgets.QMainWindow):

    purchase_text = ""

    def __init__(self):
        super(w_main, self).__init__()
        uic.loadUi('UI/w_main.ui', self)
        self.show()

        #menu supérieur
        self.b_add_user.clicked.connect(self.e_b_add_user_clicked)
        self.b_edit_user.clicked.connect(self.e_b_edit_user_clicked)
        self.b_add_menu.clicked.connect(self.e_b_add_menu_clicked)
        self.b_edit_menu.clicked.connect(self.e_b_edit_menu_clicked)

        #section employé
        self.b_select_user.clicked.connect(self.e_b_select_user_clicked)
        self.b_validate_purchase.clicked.connect(self.e_b_validate_purchase_clicked)


        #pavé numérique
        self.b_k_enter.clicked.connect(self.e_b_k_enter_clicked)
        self.b_k_cancel.clicked.connect(self.e_b_k_cancel_clicked)

        self.b_k_0.clicked.connect(self.e_b_k_0_clicked)
        self.b_k_1.clicked.connect(self.e_b_k_1_clicked)
        self.b_k_2.clicked.connect(self.e_b_k_2_clicked)
        self.b_k_3.clicked.connect(self.e_b_k_3_clicked)
        self.b_k_4.clicked.connect(self.e_b_k_4_clicked)
        self.b_k_5.clicked.connect(self.e_b_k_5_clicked)
        self.b_k_6.clicked.connect(self.e_b_k_6_clicked)
        self.b_k_7.clicked.connect(self.e_b_k_7_clicked)
        self.b_k_8.clicked.connect(self.e_b_k_8_clicked)
        self.b_k_9.clicked.connect(self.e_b_k_9_clicked)






    #Menu supérieur
    def e_b_add_user_clicked(self):
        main_app.open_w_add_user()

    def e_b_edit_user_clicked(self):
        main_app.open_w_edit_user()

    def e_b_add_menu_clicked(self):
        main_app.open_w_add_menu()

    def e_b_edit_menu_clicked(self):
        main_app.open_w_edit_menu()

    #section employé
    def e_b_select_user_clicked(self):
        current_user_datas = main_app.open_w_select_user()
        current_user_formated = "id {} : {} {}".format(current_user_datas[0][3],current_user_datas[0][0],current_user_datas[0][1])
        self.ld_current_user.setText(current_user_formated)
        self.te_purchase_recap.setText(main_app.refresh_purchase_text())

    def e_b_validate_purchase_clicked(self):

        main_app.validate_purchase()
        self.ld_current_user.setText("")
        self.ld_current_menu.setText("")
        self.te_purchase_recap.setText("Commande générée")

    #pavé numérique
    def e_b_k_enter_clicked(self):
        purchase_text = main_app.add_entry_to_purchase()
        self.te_purchase_recap.setText(purchase_text)
        self.ld_current_menu.setText("")

    def e_b_k_cancel_clicked(self):
        purchase_text = main_app.remove_entry_to_purchase()
        self.te_purchase_recap.setText(purchase_text)
        self.ld_current_menu.setText("")

    def e_b_k_0_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_0.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_1_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_1.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_2_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_2.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_3_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_3.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_4_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_4.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_5_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_5.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_6_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_6.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_7_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_7.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_8_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_8.text())
        self.ld_current_menu.setText(menu_text)

    def e_b_k_9_clicked(self):
        menu_text = main_app.add_char_current_menu(self.b_k_9.text())
        self.ld_current_menu.setText(menu_text)

    #Raccourcis clavier
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.e_b_k_1_clicked()
        if event.key() == Qt.Key_2:
            self.e_b_k_2_clicked()
        if event.key() == Qt.Key_3:
            self.e_b_k_3_clicked()
        if event.key() == Qt.Key_4:
            self.e_b_k_4_clicked()
        if event.key() == Qt.Key_5:
            self.e_b_k_5_clicked()
        if event.key() == Qt.Key_6:
            self.e_b_k_6_clicked()
        if event.key() == Qt.Key_7:
            self.e_b_k_7_clicked()
        if event.key() == Qt.Key_8:
            self.e_b_k_8_clicked()
        if event.key() == Qt.Key_9:
            self.e_b_k_9_clicked()
        if event.key() == Qt.Key_0:
            self.e_b_k_0_clicked()
        if event.key() == Qt.Key_Enter:
            self.e_b_k_enter_clicked()
        if event.key() == Qt.Key_Delete:
            self.e_b_k_cancel_clicked()
