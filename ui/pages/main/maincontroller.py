from ui.pages.main.mainpage import MainPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class MainController(PageControllerBase):
    page: MainPage
    model: Model
    def __init__(self):
        super().__init__()
        self.page = MainPage()
        self.model = Model()
    def initLogic(self):
        pass