from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.Qt import Qt

import main_app


class w_get_id(QtWidgets.QDialog):
    def __init__(self):
        super(w_get_id, self).__init__()
        uic.loadUi('UI/w_id.ui', self)


        self.le_id.setFocus()


        self.b_kid_0.clicked.connect(self.e_b_kid_0_clicked)
        self.b_kid_1.clicked.connect(self.e_b_kid_1_clicked)
        self.b_kid_2.clicked.connect(self.e_b_kid_2_clicked)
        self.b_kid_3.clicked.connect(self.e_b_kid_3_clicked)
        self.b_kid_4.clicked.connect(self.e_b_kid_4_clicked)
        self.b_kid_5.clicked.connect(self.e_b_kid_5_clicked)
        self.b_kid_6.clicked.connect(self.e_b_kid_6_clicked)
        self.b_kid_7.clicked.connect(self.e_b_kid_7_clicked)
        self.b_kid_8.clicked.connect(self.e_b_kid_8_clicked)
        self.b_kid_9.clicked.connect(self.e_b_kid_9_clicked)


    def set_id(self,to_set):
        if self.le_id.text() != "" or to_set != "0":
            self.le_id.setText(self.le_id.text() + to_set)

    def e_b_kid_0_clicked(self):
        menu_text = self.b_kid_0.text()
        self.set_id(menu_text)

    def e_b_kid_1_clicked(self):
        menu_text = self.b_kid_1.text()
        self.set_id(menu_text)

    def e_b_kid_2_clicked(self):
        menu_text = self.b_kid_2.text()
        self.set_id(menu_text)

    def e_b_kid_3_clicked(self):
        menu_text = self.b_kid_3.text()
        self.set_id(menu_text)

    def e_b_kid_4_clicked(self):
        menu_text = self.b_kid_4.text()
        self.set_id(menu_text)

    def e_b_kid_5_clicked(self):
        menu_text = self.b_kid_5.text()
        self.set_id(menu_text)

    def e_b_kid_6_clicked(self):
        menu_text = self.b_kid_6.text()
        self.set_id(menu_text)

    def e_b_kid_7_clicked(self):
        menu_text = self.b_kid_7.text()
        self.set_id(menu_text)

    def e_b_kid_8_clicked(self):
        menu_text = self.b_kid_8.text()
        self.set_id(menu_text)

    def e_b_kid_9_clicked(self):
        menu_text = self.b_kid_9.text()
        self.set_id(menu_text)



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.e_b_kid_1_clicked()
        if event.key() == Qt.Key_2:
            self.e_b_kid_2_clicked()
        if event.key() == Qt.Key_3:
            self.e_b_kid_3_clicked()
        if event.key() == Qt.Key_4:
            self.e_b_kid_4_clicked()
        if event.key() == Qt.Key_5:
            self.e_b_kid_5_clicked()
        if event.key() == Qt.Key_6:
            self.e_b_kid_6_clicked()
        if event.key() == Qt.Key_7:
            self.e_b_kid_7_clicked()
        if event.key() == Qt.Key_8:
            self.e_b_kid_8_clicked()
        if event.key() == Qt.Key_9:
            self.e_b_kid_9_clicked()
        if event.key() == Qt.Key_0:
            self.e_b_kid_0_clicked()
