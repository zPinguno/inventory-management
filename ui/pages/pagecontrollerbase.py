from type.user import User
from type.userrole import UserRole
from ui.pages.pageBase import PageBase

class PageControllerBase:
    page: PageBase

    fCurrentUser: User

    isInitialized:bool = False
    isCurrentlyWorking: bool
    refreshIsCurrentlyWorking: callable
    def __init__(self, selectPage, refreshIsCurrentlyWorking):
        self.selectPage = selectPage
        self.refreshIsCurrentlyWorking = refreshIsCurrentlyWorking

        pass
    def detachHandlers(self):
        pass
    def showPage(self):
        if not self.isInitialized:
            self.page.initComponents()
        else:
            self.detachHandlers()
        self.initLogic()
        self.page.show()
    def hidePage(self):
        self.page.hide()
        self.page.deInitComponents()
    def initLogic(self):
        self.showSwitchPageButton()
        self.isInitialized = True
    def getPage(self):
        return self.page
    def showSwitchPageButton(self):
        if UserRole.ADMIN in self.fCurrentUser.roles:
            self.page.fSwitchSiteButton.show()
        else:
            self.page.fSwitchSiteButton.hide()
    def loginUser(self, user: User):
        self.fCurrentUser = user