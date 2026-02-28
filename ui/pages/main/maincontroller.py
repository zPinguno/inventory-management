from ast import List
from multiprocessing.spawn import prepare
from typing import Any

from PyQt6.QtWidgets import QTableWidgetItem

from type.itemheader import ItemHeader
from type.itemstate import ItemState, getAllStates, getAllStatesAsStrings
from type.tableitem import TableItem
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
        self.refreshFilter()
        self.refreshItems()

    def initDialogLogic(self):
        self.fDialog.fStateDropdown.currentIndexChanged.connect(self.onStateChanged)
        self.fDialog.fSaveButton.clicked.connect(self.onSaveItem)

    def onStateChanged(self):
        if self.fDialog.fStateDropdown.currentText() == ItemState.BORROWED.value:
            self.fDialog.fLocationDropdown.hide()
            self.fDialog.fLocationLabel.hide()
        else:
            self.fDialog.fLocationDropdown.show()
            self.fDialog.fLocationLabel.show()

    def showAddItemDialog(self):
        self.fDialog = AddItem(self.model, self.getBaseDataAsStrings)
        self.initDialogLogic()
        if self.fDialog.exec():
            return
    def onSaveItem(self):
        self.model.items.append(self.fDialog.getResult())
        self.model.save()
        self.refreshItems()
        self.fDialog.close()
    def refreshItems(self):
        self.model.load()
        self.items = self.model.items
        self.refreshTable()
    def refreshTable(self):
        preparedItems = self.prepareItemsForTable()
        self.page.fTable.setRowCount(len(preparedItems))
        for i in range(len(preparedItems)):
            self.page.fTable.setItem(i, 0, preparedItems[i].object)
            self.page.fTable.setItem(i, 1, preparedItems[i].group)
            self.page.fTable.setItem(i, 2, preparedItems[i].subject)
            self.page.fTable.setItem(i, 3, preparedItems[i].location)
            self.page.fTable.setItem(i, 4, preparedItems[i].department)
            self.page.fTable.setItem(i, 5, preparedItems[i].state)
            self.page.fTable.setItem(i, 6, preparedItems[i].responsiblePerson)

    def prepareItemsForTable(self):
        preparedItems = list()
        for item in self.items:
            object = QTableWidgetItem(item.object.getName())
            group = QTableWidgetItem(item.group.getName())
            subject = QTableWidgetItem(item.subject.getName())
            location = QTableWidgetItem(item.location.getName())
            department = QTableWidgetItem(item.department.getName())
            state = QTableWidgetItem(item.state.value)
            responsiblePerson = QTableWidgetItem(item.responsiblePerson.userName)
            preparedItems.append(TableItem(object, group, subject, location, department, state, responsiblePerson))
        return preparedItems

    def refreshFilter(self):
        currentFilter = self.page.fFilterDropDown.currentText()
        searchOptions = self.getSearchOptionsForFilter(ItemHeader(currentFilter))
        self.page.fFilterSearchDropDown.clear()
        self.page.fFilterSearchDropDown.addItems(searchOptions)

    def getSearchOptionsForFilter(self, filter: ItemHeader):
        self.model.load()
        match filter:
            case ItemHeader.OBJECT:
                return self.getBaseDataAsStrings(self.model.getAllObjects())
            case ItemHeader.GROUP:
                return self.getBaseDataAsStrings(self.model.getAllGroups())
            case ItemHeader.DEPARTMENT:
                return self.getBaseDataAsStrings(self.model.getAllDepartments())
            case ItemHeader.LOCATION:
                return self.getBaseDataAsStrings(self.model.getAllLocations())
            case ItemHeader.RESPONSIBLE:
                return self.model.getAllResponsibleUserNames()
            case ItemHeader.SUBJECT:
                return self.getBaseDataAsStrings(self.model.getAllSubjects())
            case ItemHeader.STATE:
                return getAllStatesAsStrings()


    def getBaseDataAsStrings(self, baseDataList: list[Any]):
        strings = list()
        for baseData in baseDataList:
            strings.append(baseData.name)

        return strings

