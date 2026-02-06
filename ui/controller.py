from ui.pages.login.logincontroller import LoginController


class Controller:
    fLoginPageController: LoginController
    def __init__(self):
        self.fLoginPageController = LoginController()
        self.fLoginPageController.showPage()