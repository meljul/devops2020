from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_app


class w_add_user(QtWidgets.QDialog):

    def __init__(self):
        super(w_add_user, self).__init__()
        uic.loadUi('UI/w_add_user.ui', self)
        self.buttonBox.accepted.connect(self.e_b_accepted)
        self.maj = False
        self.init_keyboard()

    def e_b_accepted(self):
        user_name = self.le_name.text()
        user_surname = self.le_surname.text()
        user_email = self.le_email.text()

        main_app.add_user(user_name,user_surname,user_email)

    def init_keypad(self):

        for button in self.keypad.parentWidget().findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.on_click_keypad)


    def on_click_keypad(self):
        # récupère le nom du bouton cliquer et ignore les 7 premier char ('button_')

        sender = self.sender().objectName()[7:]
        if sender not in ['maj', 'del']:
            for input_field in self.input_layout.parentWidget().findChildren(QtWidgets.QLineEdit):
                new_text = ''
                if input_field.hasFocus():
                    current_text = input_field.text()
                    if input_field.objectName() == 'text_price':
                        if sender in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                            new_text = current_text + sender
                        elif sender == 'point' and '.' not in current_text:
                            new_text = current_text + '.'
                    elif sender not in ['arobase', 'under', 'point', 'tirret']:
                        if self.maj:
                            new_text = current_text + sender.upper()
                        else:
                            new_text = current_text + sender
                    elif sender == 'arobase':
                        new_text = current_text + '@'
                    elif sender == 'point':
                        new_text = current_text + '.'
                    elif sender == 'tirret':
                        new_text = current_text + '-'
                    elif sender == 'under':
                        new_text = current_text + "_"

                    if new_text != '':
                        input_field.setText(new_text)
                    break

    def init_keyboard(self):

        self.init_keypad()
        self.button_maj.clicked.connect(self.on_click_maj)
        self.button_del.clicked.connect(self.on_click_del)

    def on_click_maj(self):

        if self.maj:
            self.maj = False
        else:
            self.maj = True

    def on_click_del(self):
        for input_field in self.input_layout.parentWidget().findChildren(QtWidgets.QLineEdit):
            if input_field.hasFocus():
                if input_field.text() != '':
                    input_field.setText(input_field.text()[:-1])
