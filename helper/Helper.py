from ui.controller import Controller
from ui.pages.admin.adminpage import AdminPage
from ui.pages.login.loginpage import LoginPage
from ui.pages.main.mainpage import MainPage
from ui.pages.pageBase import PageBase


def getControllerByPage(page:PageBase, this:Controller):
    if isinstance(page, LoginPage):
        return this.fLoginPageController
    if isinstance(page, MainPage) :
        return this.fMainPageController
    if isinstance(page, AdminPage) :
        return this.fAdminPageController
    return None