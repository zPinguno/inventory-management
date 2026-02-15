from ui.pages.pageBase import PageBase

class PageControllerBase:
    page: PageBase
    def __init__(self):
        pass
    def showPage(self):
        self.page.initComponents()
        self.initLogic()
    def hidePage(self):
        self.page.hide()
    def initLogic(self):
        pass