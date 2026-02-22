from type.itemheader import ItemHeader
from ui.pages.main.mainpage import MainPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class MainController(PageControllerBase):
    page: MainPage
    #addUserDialog: AddUserDialog
    model: Model
    def __init__(self):
        super().__init__()
        self.page = MainPage()
        self.model = Model()
    def initLogic(self):
        self.selectInputForMainPage()

    def selectInputForMainPage(self):
    
        self.page.fResponsiblePersonDropDown.hide()
        self.page.fStateDropDown.hide()
        self.page.fFilterInput.hide()
    
        currentFilterDropDown = self.page.fFilterDropDown.currentText()
        match currentFilterDropDown:
            case ItemHeader.RESPONSIBLE.value:
                self.page.fResponsiblePersonDropDown.show()
            case ItemHeader.STATE.value:
                self.page.fStateDropDown.show()
            case _:
                self.page.fFilterInput.show()
