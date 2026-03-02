from type.user import User
from type.userrole import UserRole
from ui.dialogs.dialogBase import DialogBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

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
    fAdminCheckbox: QCheckBox
    fResponsiblePersonCheckbox: QCheckBox
    fTeacherCheckbox: QCheckBox
    
    user: User | None

    def __init__(self):
        super().__init__()
        self.user = None
        self.width = 140
        self.height = 350
        self.setWindowTitle("Neuen Benutzer hinzufügen")
        self.setFixedSize(self.width, self.height)
        
    def initComponents(self):
        super().initComponents()
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fRoleOptions = []
        self.fVLayout = QVBoxLayout()

        self.fFirstNameLabel = createText('Vorname', self.fVLayout)
        self.fFirstNameInput = createInput(self, 'Vorname', self.fVLayout)

        self.fLastNameLabel = createText('Nachname', self.fVLayout)
        self.fLastNameInput = createInput(self, 'Nachname', self.fVLayout)

        self.fUserNameLabel = createText('Benutzername', self.fVLayout)
        self.fUserNameInput = createInput(self, 'Benutzername', self.fVLayout)

        self.fPasswordLabel = createText('Passwort', self.fVLayout)
        self.fPasswordInput = createInput(self, 'Passwort', self.fVLayout)
        
        self.fAdminCheckbox = createCheckbox(self, UserRole.ADMIN.value, self.fVLayout)
        self.fResponsiblePersonCheckbox = createCheckbox(self, UserRole.RESPONSIBLE.value, self.fVLayout)
        self.fTeacherCheckbox = createCheckbox(self, UserRole.TEACHER.value, self.fVLayout)

        self.fSaveButton = createButton(self, 'Speichern', self.fVLayout)

        self.fCenterWidget = QWidget(self)


        self.prepareWidgets()
    def prepareWidgets(self):
        self.fPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.fCenterWidget.setLayout(self.fVLayout)
        self.fVLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def prepareStyles(self):
        pass # Ehrlich, keine Ahnung für Styles
        

    def loadStyleSheet(self):
        styleSheet = open('./ui/dialogs/addUser/addUser.css').read()
        self.setStyleSheet(styleSheet)