from type.userrole import UserRole
from ui.pages.login.logincontroller import LoginController
from ui.pages.main.maincontroller import MainController
from type.user import User
from model.model import Model
import hashlib

class Controller:
    fCurrentUser: User
    model: Model
    fLoginPageController: LoginController
    fMainPageController: MainController
    def __init__(self):
        self.model = Model()
        self.createUsers()
        self.fLoginPageController = LoginController()
        self.fMainPageController = MainController()
        self.fLoginPageController.showPage()
        self.fLoginPageController.page.fLoginButton.clicked.connect(self.onLogin)
        self.fLoginPageController.page.fPassword.returnPressed.connect(self.onLogin)
    
    def initMainPageEvents(self):
        self.fMainPageController.page.fFilterDropDown.currentIndexChanged.connect(self.fMainPageController.selectInputForMainPage)

    def onLogin(self):
        username = self.fLoginPageController.page.fUserName.text()
        password = self.fLoginPageController.page.fPassword.text()
        user = self.model.login(username, self.hashPassword(password))
        if (user != None):
            self.fCurrentUser = user
            self.fLoginPageController.hidePage()
            self.fMainPageController.showPage()
            self.initMainPageEvents()
        else:
            self.fLoginPageController.showLoginError()

    def createUsers(self):
        if self.model.users.__len__() > 0:
            return
        self.model.addUser(User('b', 'd', 'r', self.hashPassword('Hallo123#'), UserRole.RESPONSIBLE))
        self.model.addUser(User('b', 'd', 't', self.hashPassword('Hallo123#'), UserRole.TEACHER))
        self.model.addUser(User('b', 'd', 'a', self.hashPassword('Hallo123#'), UserRole.ADMIN))
        self.model.save()
    
    def hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()