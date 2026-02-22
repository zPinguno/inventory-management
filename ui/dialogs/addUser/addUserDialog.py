from model.model import Model
from type.user import User
from type.userrole import UserRole
from ui.dialogs.dialogBase import DialogBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from type.itemheader import ItemHeader
from type.itemstate import ItemState
from typing import List

from ui.widgetcreationhelper import createCheckbox, createInput, createButton, createText


class AddUser(DialogBase):
    fVLayout = QVBoxLayout    
    fFirstNameInput: QLineEdit
    fLastNameInput: QLineEdit
    fUserNameInput: QLineEdit
    fPasswordInput: QLineEdit
    fFirstNameLabel: QLabel
    fLastNameLabel: QLabel
    fUserNameLabel: QLabel
    fPasswordLabel: QLabel
    fRoleDropDown: QComboBox
    fSaveButton: QPushButton
    fRoleOptions: List[QCheckBox] = []
    
    user: User | None

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Neuen Benutzer hinzufügen')
        self.user = None
        
    def initComponents(self):
        super().initComponents()
        self.setWindowTitle('Add User')
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fRoleOptions = []
        self.fVLayout = QVBoxLayout()

        self.fFirstNameLabel = createText('Vorname', self.fVLayout)
        self.fFirstNameInput = createInput(self, 'Vorname', self.fVLayout)

        self.fLastNameLabel = createText('Nachname', self.fVLayout)
        self.fLastNameLabel = createInput(self, 'Nachname', self.fVLayout)

        self.fUserNameLabel = createText('Benutzername', self.fVLayout)
        self.fUserNameInput = createInput(self, 'Benutzername', self.fVLayout)

        self.fPasswordInput = createText('Passwort', self.fVLayout)
        self.fPasswordLabel = createInput(self, 'Passwort', self.fVLayout)
        
        self.createAllCheckboxes()

        self.fSaveButton = createButton(self, 'Speichern')


        self.prepareWidgets()
    def prepareWidgets(self):
        self.fPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)
    def prepareStyles(self):
        pass

    def createAllCheckboxes(self):
        userRoleList = [member.value for member in UserRole]
        for userRole in userRoleList:
            self.fRoleOptions.append(createCheckbox(self, userRole, self.fVLayout))
        

    def loadStyleSheet(self):
        styleSheet = open('./ui/dialogs/addUser/addUser.css').read()
        self.setStyleSheet(styleSheet)