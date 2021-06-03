from screens.ui.UI_NewUser import UI_NewUser
from PyQt5 import QtCore, QtWidgets
import sqlite3

class Newuser(QtWidgets.QWidget, UI_NewUser):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Back.clicked.connect(self.back_handler)
        self.btn_submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def btn_submit_handler(self):
        self.create_db_newuser()

    def back_handler(self):
        self.switch_window.emit()

    def create_db_newuser(self):

        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_phone_v = self.txt_phone.text()
        txt_emailid_v = self.txt_email.text()
        txt_username_v = self.txt_username.text()
        txt_password_v = self.lineEdit.text()

        if (len(txt_firstname_v) <= 1
                and len(txt_lastname_v) <= 1 and
                len(txt_phone_v) <= 9 and
                len(txt_emailid_v) <= 1 and
                len(txt_username_v) <= 1 and
                len(txt_password_v) <= 1):

            """
            Logic to see if users Enter all Feilds Correctly 
            """
            self.pop_message(text="Please Enter All Feilds ")

        else:

            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    fname TEXT, 
                    lname TEXT, 
                    Phone TEXT, 
                    email TEXT,
                    username TEXT, 
                    password TEXT)""")

            cursor.execute(""" INSERT INTO credentials 
                    (fname,
                    lname,
                    Phone,
                    email,
                    username, 
                    password)

                VALUES 
                (?,?,?,?,?,?)
                """, (txt_firstname_v, txt_lastname_v, txt_phone_v, txt_emailid_v, txt_username_v, txt_password_v))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message(text="Added to Database ! ")