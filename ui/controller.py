from type.userrole import UserRole
from ui.pages.login.logincontroller import LoginController
from ui.pages.main.maincontroller import MainController
from ui.pages.admin.admincontroller import AdminController
from type.user import User
from model.model import Model
from helper.Helper import hashPassword

from ui.pages.pageBase import PageBase
from helper.Helper import getControllerByPage

class Controller:
    fCurrentUser: User
    model: Model
    fLoginPageController: LoginController
    fMainPageController: MainController
    fAdminPageController: AdminController

    isCurrentlyWorking: bool
    isInitialized: bool

    fCurrentPage: PageBase
    def __init__(self):
        self.isInitialized = False

        self.model = Model()
        self.createUsers()
        self.fLoginPageController = LoginController(self.selectPage, self.refreshIsCurrentlyWorkingForPageController,self.onLogin)
        self.fMainPageController = MainController(self.selectPage, self.refreshIsCurrentlyWorkingForPageController, self.showLoginPage)
        self.fAdminPageController = AdminController(self.selectPage, self.refreshIsCurrentlyWorkingForPageController, self.showLoginPage)
        self.showLoginPage()
        self.isInitialized = True
        self.refreshIsCurrentlyWorkingForPageController(False)

    def refreshIsCurrentlyWorkingForPageController(self, working:bool):
        self.isCurrentlyWorking = working
        self.fLoginPageController.isCurrentlyWorking = self.isCurrentlyWorking
        self.fMainPageController.isCurrentlyWorking = self.isCurrentlyWorking
        self.fAdminPageController.isCurrentlyWorking = self.isCurrentlyWorking

    def showLoginPage(self):
        self.fCurrentUser = None
        self.selectPage("Login")
    
    def selectPage(self, pageName = "Main"):
        if self.isInitialized:
            currentController = getControllerByPage(self.fCurrentPage, self)
            currentController.hidePage()

        match pageName:
            case "Login":
                self.fCurrentPage = self.fLoginPageController.page
                self.fLoginPageController.showPage()

            case "Main":
                self.fCurrentPage = self.fMainPageController.page
                self.fMainPageController.showPage()

            case "Admin":
               self.fCurrentPage = self.fAdminPageController.page
               self.fAdminPageController.showPage()
    def loginUser(self, user:User):
        self.fCurrentUser = user
        self.fMainPageController.loginUser(user)
        self.fAdminPageController.loginUser(user)

    def onLogin(self):
        self.model.load()
        username = self.fLoginPageController.page.fUserName.text()
        password = self.fLoginPageController.page.fPassword.text()
        user = self.model.login(username, hashPassword(password))
        if user != None:
            self.loginUser(user)
            self.selectPage("Main")
        else:
            self.fLoginPageController.showLoginError()

    def createUsers(self):
        if self.model.users.__len__() > 0:
            return
        self.model.addUser(User('b', 'd', 'r', hashPassword('Hallo123#'), [UserRole.RESPONSIBLE, UserRole.ADMIN]))
        self.model.addUser(User('b', 'd', 't', hashPassword('Hallo123#'), [UserRole.TEACHER]))
        self.model.addUser(User('b', 'd', 'a', hashPassword('Hallo123#'), [UserRole.ADMIN]))
        self.model.save()