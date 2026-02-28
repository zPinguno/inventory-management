from PyQt6.QtWidgets import QTableWidgetItem


class TableItem():
    object: QTableWidgetItem
    group: QTableWidgetItem
    subject: QTableWidgetItem
    location: QTableWidgetItem
    department: QTableWidgetItem
    state: QTableWidgetItem
    responsiblePerson: QTableWidgetItem
    def __init__(self, obj:QTableWidgetItem, group:QTableWidgetItem, department:QTableWidgetItem, subject:QTableWidgetItem, location:QTableWidgetItem, responsiblePerson:QTableWidgetItem, state:QTableWidgetItem):
        self.object = obj
        self.group = group
        self.department = department
        self.subject = subject
        self.location = location
        self.responsiblePerson = responsiblePerson
        self.state = state
