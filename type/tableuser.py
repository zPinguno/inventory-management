from PyQt6.QtWidgets import QTableWidgetItem

class TableItem():
    firstname: QTableWidgetItem
    lastname: QTableWidgetItem
    userName: QTableWidgetItem
    usertype: QTableWidgetItem
    def __init__(self, firstname:QTableWidgetItem, lastname:QTableWidgetItem, userName:QTableWidgetItem, usertype:QTableWidgetItem):
        self.firstname = firstname
        self.lastname = lastname
        self.userName = userName
        self.usertype = usertype
