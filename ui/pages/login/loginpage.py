from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *

from ui.widgetcreationhelper import createInput, createTitle, createButton


class LoginPage(PageBase):
    fLoginButton:QPushButton
    fUserName: QLineEdit
    fPassword: QLineEdit
    fVLayout: QVBoxLayout
    fTitle: QLabel
    fCenterWidget: QWidget
    def __init__(self):
        super().__init__()
    def initComponents(self):
        super().initComponents()
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fVLayout = QVBoxLayout()
        self.fUserName = createInput(self, 'Benutzername', self.fVLayout)
        self.fPassword = createInput(self, 'Passwort',self.fVLayout)
        self.fLoginButton = createButton(self, 'Anmelden',self.fVLayout)
        self.fTitle = createTitle('Willkommen!',self.fVLayout)
        self.fCenterWidget = QWidget(self)
        self.prepareWidgets()
    def prepareWidgets(self):
        self.prepareStyles()
        self.fPassword.setEchoMode(QLineEdit.EchoMode.Password)
    def prepareStyles(self):
        self.fVLayout.setProperty('class', 'VLayout')
        self.fUserName.setProperty('class', 'loginElements')
        self.fPassword.setProperty('class', 'loginElements')
        self.fLoginButton.setProperty('class', 'loginElements')
        self.fCenterWidget.setProperty('class', 'loginPage')

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/login/login.css').read()
        self.setStyleSheet(styleSheet)
