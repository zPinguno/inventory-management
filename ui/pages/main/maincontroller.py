from type.itemheader import ItemHeader
from ui.dialogs.addUser.addUserController import AddUserController
from ui.pages.main.mainpage import MainPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class MainController(PageControllerBase):
    page: MainPage
    addUserDialogController: AddUserController
    model: Model
    def __init__(self):
        super().__init__()
        self.page = MainPage()
        self.model = Model()
        self.addUserDialog = AddUserController()
    def initLogic(self):
        self.selectInputForMainPage()
        self.page.fAddItemButton.clicked.connect(self.showAddUserDialog)


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
    def showAddUserDialog(self):
        self.addUserDialog.showDialog()
