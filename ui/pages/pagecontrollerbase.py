from type.user import User
from type.userrole import UserRole
from ui.pages.pageBase import PageBase

class PageControllerBase:
    page: PageBase

    fCurrentUser: User

    def __init__(self, selectPage):
        self.selectPage = selectPage
        pass
    def showPage(self):
        self.page.initComponents()
        self.initLogic()
    def hidePage(self):
        self.page.hide()
        self.page.deInitComponents()
    def initLogic(self):
        self.showSwitchPageButton()
    def getPage(self):
        return self.page
    def showSwitchPageButton(self):
        if UserRole.ADMIN in self.fCurrentUser.roles:
            self.page.fSwitchSiteButton.show()
        else:
            self.page.fSwitchSiteButton.hide()
    def loginUser(self, user: User):
        self.fCurrentUser = user