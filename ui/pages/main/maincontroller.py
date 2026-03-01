from ast import List
from multiprocessing.spawn import prepare
from typing import Any

from PyQt6.QtWidgets import QTableWidgetItem

from type.item import Item
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
    items: list[Item]
    def __init__(self, selectPage):
        super().__init__(selectPage)
        self.model = Model()
        self.page = MainPage(self.model)


    def initLogic(self):
        super().initLogic()
        self.page.fAddItemButton.clicked.connect(self.showAddItemDialog)
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Admin"))
        self.page.fFilterDropDown.currentIndexChanged.connect(self.refreshFilter)
        self.page.fFilterSearchButton.clicked.connect(self.onSearch)
        self.refreshFilter()
        self.refreshItems()
    def onSearch(self):
        self.refreshTableWithItems(self.prepareItemsForTable(self.getSearchParamForItems()))
    def getItemsBySearchParam(self, searchParam: Any):
        items = list()
        searchFilter = self.page.fFilterDropDown.currentText()

        if not isinstance(searchParam, str):
            searchParam = searchParam.getName()

        for item in self.items:
            match searchFilter:
                case ItemHeader.OBJECT.value:
                    if item.object.getName() == searchParam:
                        items.append(item)
                case ItemHeader.GROUP.value:
                    if item.group.getName() == searchParam:
                        items.append(item)
                case ItemHeader.DEPARTMENT.value:
                    if item.department.getName() == searchParam:
                        items.append(item)
                case ItemHeader.SUBJECT.value:
                    if item.subject.getName() == searchParam:
                        items.append(item)
                case ItemHeader.LOCATION.value:
                    if item.location.getName() == searchParam:
                        items.append(item)
                case ItemHeader.RESPONSIBLE.value:
                    if item.responsiblePerson.getUserName() == searchParam:
                        items.append(item)
                case ItemHeader.STATE.value:
                    if item.state == searchParam:
                        items.append(item)
        return items
    def getSearchParamForItems(self):
        searchFilter = self.page.fFilterDropDown.currentText()
        searchValue = self.page.fFilterSearchDropDown.currentText()

        match searchFilter:
            case ItemHeader.OBJECT.value:
                return self.getItemsBySearchParam(self.findBaseDataByString(self.model.getAllObjects(), searchValue))
            case ItemHeader.GROUP.value:
                return self.getItemsBySearchParam(self.findBaseDataByString(self.model.getAllGroups(), searchValue))
            case ItemHeader.DEPARTMENT.value:
                return self.getItemsBySearchParam(self.findBaseDataByString(self.model.getAllDepartments(), searchValue))
            case ItemHeader.LOCATION.value:
                return self.getItemsBySearchParam(self.findBaseDataByString(self.model.getAllLocations(), searchValue))
            case ItemHeader.RESPONSIBLE.value:
                return self.getItemsBySearchParam(self.model.getUserByUserName(searchValue))
            case ItemHeader.SUBJECT.value:
                return self.getItemsBySearchParam(self.findBaseDataByString(self.model.getAllSubjects(), searchValue))
            case ItemHeader.STATE.value:
                return self.getItemsBySearchParam(self.findStatesByString(searchValue))
            case _:
                return self.items
    def findStatesByString(self, state: str):
        for itemState in getAllStates():
            if itemState.value == state:
                return itemState
        return ItemState.USED

    def findBaseDataByString(self, baseDataList: list[Any], searchValue: str):
        for baseData in baseDataList:
            if searchValue in baseData.name:
                return baseData
        return None
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
        preparedItems = self.prepareItemsForTable(self.items)
        self.refreshTableWithItems(preparedItems)

    def refreshTableWithItems(self, items: list[QTableWidgetItem]):
        self.page.fTable.setRowCount(len(items))
        for i in range(len(items)):
            self.page.fTable.setItem(i, 0, items[i].object)
            self.page.fTable.setItem(i, 1, items[i].group)
            self.page.fTable.setItem(i, 2, items[i].subject)
            self.page.fTable.setItem(i, 3, items[i].location)
            self.page.fTable.setItem(i, 4, items[i].department)
            self.page.fTable.setItem(i, 5, items[i].state)
            self.page.fTable.setItem(i, 6, items[i].responsiblePerson)

    def prepareItemsForTable(self, items: list[Item]):
        preparedItems = list()
        for item in items:
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

