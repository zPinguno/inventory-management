from type.itemheader import ItemHeader
from type.itemstate import ItemState, getAllStates, getAllStatesAsStrings
from type.user import User

from ui.dialogs.addItem.addItem import AddItem
from ui.pages.main.mainpage import MainPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class MainController(PageControllerBase):
    page: MainPage
    model: Model
    fDialog: AddItem

    def __init__(self, selectPage):
        super().__init__(selectPage)
        self.model = Model()
        self.page = MainPage(self.model)


    def initLogic(self):
        super().initLogic()
        self.page.fAddItemButton.clicked.connect(self.showAddItemDialog)
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Admin"))
        self.page.fFilterDropDown.currentIndexChanged.connect(self.refreshFilter)

    def initDialogLogic(self):
        self.fDialog.fStateDropdown.currentIndexChanged.connect(self.onStateChanged)

    def onStateChanged(self):
        if self.fDialog.fStateDropdown.currentText() == ItemState.BORROWED.value:
            self.fDialog.fLocationDropdown.hide()
            self.fDialog.fLocationLabel.hide()
        else:
            self.fDialog.fLocationDropdown.show()
            self.fDialog.fLocationLabel.show()

    def showAddItemDialog(self):
        self.fDialog = AddItem(self.model)
        self.initDialogLogic()
        if self.fDialog.exec():
            self.fDialog

    def refreshFilter(self):
        currentFilter = self.page.fFilterDropDown.currentText()
        searchOptions = self.getSearchOptionsForFilter(ItemHeader(currentFilter))
        self.page.fFilterSearchDropDown.clear()
        self.page.fFilterSearchDropDown.addItems(searchOptions)

    def getSearchOptionsForFilter(self, filter: ItemHeader):
        self.model.load()
        match filter:
            case ItemHeader.OBJECT:
                return self.model.getAllObjects()
            case ItemHeader.GROUP:
                return self.model.getAllGroups()
            case ItemHeader.DEPARTMENT:
                return self.model.getAllDepartments()
            case ItemHeader.LOCATION:
                return self.model.getAllLocations()
            case ItemHeader.RESPONSIBLE:
                return self.model.getAllResponsibleUserNames()
            case ItemHeader.STATE:
                return getAllStatesAsStrings()
        return list()

