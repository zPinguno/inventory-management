from ui.pages.login.loginpage import LoginPage
from ui.pages.pagecontrollerbase import PageControllerBase
from PyQt6.QtWidgets import QMessageBox
from model.model import Model

class LoginController(PageControllerBase):
    page: LoginPage
    model: Model
    def __init__(self):
        super().__init__()
        self.page = LoginPage()
    def initLogic(self):
        pass

    def showLoginError(self):
        errorDialog = QMessageBox(self.page)
        errorDialog.setIcon(QMessageBox.Icon.Warning)
        errorDialog.setWindowTitle('Login Fehler')
        errorDialog.setText('Falscher Benutzername oder Passwort!')
        errorDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        errorDialog.exec()
