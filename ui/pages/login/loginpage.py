from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

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
        self.fTitle = createTitle('Willkommen!',self.fVLayout)

        self.fUserName = createInput(self, 'Benutzername', self.fVLayout)
        self.fPassword = createInput(self, 'Passwort',self.fVLayout)
        self.fLoginButton = createButton(self, 'Anmelden',self.fVLayout)
        self.fCenterWidget = QWidget(self)

        self.prepareWidgets()
    def prepareWidgets(self):
        self.prepareStyles()
        self.fPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.fCenterWidget.setLayout(self.fVLayout)
        self.fVLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fCenterWidget.setGraphicsEffect(self.setBoxShadow())
        self.setCentralWidget(self.fCenterWidget)
    def prepareStyles(self):
        self.fUserName.setProperty('class', 'loginElements')
        self.fPassword.setProperty('class', 'loginElements')
        self.fLoginButton.setProperty('class', 'loginElements')
        self.fCenterWidget.setProperty('class', 'loginPage')
    
    def setBoxShadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)  
        shadow.setColor(QColor(0, 0, 0, 80))
        return shadow

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/login/login.css').read()
        self.setStyleSheet(styleSheet)
