from type.itemheader import ItemHeader
from type.user import User

from ui.dialogs.addItem.addItem import AddItem
from ui.pages.main.mainpage import MainPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class MainController(PageControllerBase):
    page: MainPage
    model: Model

    def __init__(self, selectPage):
        super().__init__(selectPage)
        self.model = Model()
        self.page = MainPage(self.model)


    def initLogic(self):
        super().initLogic()
        self.selectInputForMainPage()
        self.page.fAddItemButton.clicked.connect(self.showAddItemDialog)
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Admin"))


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
    def showAddItemDialog(self):
        dialog = AddItem(self.model)

        if dialog.exec():
            dialog

