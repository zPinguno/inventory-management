from ui.pages.login.loginpage import LoginPage
from ui.pages.pagecontrollerbase import PageControllerBase


class LoginController(PageControllerBase):
    def __init__(self):
        super().__init__()
        self.page = LoginPage()
    def initLogic(self):
        pass