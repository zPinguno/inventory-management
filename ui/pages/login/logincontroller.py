from ui.pages.login.loginpage import LoginPage
from ui.pages.pagecontrollerbase import PageControllerBase
from PyQt6.QtWidgets import QMessageBox
from model.model import Model

class LoginController(PageControllerBase):
    page: LoginPage
    model: Model
    def __init__(self, selectPage, refreshIsCurrentlyWorking, onLogin):
        self.page = LoginPage()
        super().__init__(selectPage, refreshIsCurrentlyWorking)
        self.onLogin = onLogin
    def initLogic(self):
        self.page.fLoginButton.clicked.connect(self.onLogin)
        self.page.fPassword.returnPressed.connect(self.onLogin)

    def detachHandlers(self):
        self.page.fLoginButton.clicked.disconnect()
        self.page.fPassword.returnPressed.disconnect()
    def showLoginError(self):
        errorDialog = QMessageBox(self.page)
        errorDialog.setIcon(QMessageBox.Icon.Warning)
        errorDialog.setWindowTitle('Login Fehler')
        errorDialog.setText('Falscher Benutzername oder Passwort!')
        errorDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        errorDialog.exec()
