from PyQt6.QtWidgets import QTableWidgetItem
from ui.dialogs.element.masterDataDialog import MasterDataDialog
from ui.pages.admin.adminpage import AdminPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model
from type.location import Location
from type.subject import Subject
from type.group import Group
from type.object import Object
from type.department import Department

class AdminController(PageControllerBase):
    page: AdminPage
    model: Model
    object: Object
    subject: Subject
    location: Location
    department: Department
    group: Group
    masterDataDialog: MasterDataDialog
    databaseTable: str
    def __init__(self, selectPage):
        super().__init__(selectPage)
        self.page = AdminPage()
        self.model = Model()
    def initLogic(self):
        self.checkTable()
        self.page.fDropDownMenu.currentIndexChanged.connect(self.checkTable)
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Main"))
        self.page.fAddItemButton.clicked.connect(self.showDialog)

    def showDialog(self):
        self.masterDataDialog = MasterDataDialog(self.databaseTable)
        self.masterDataDialog.show()
        self.masterDataDialog.fSafeButton.clicked.connect(self.safeEntry)
    
    def safeEntry(self):
        name = self.masterDataDialog.fNameInput.text()
        match self.databaseTable:
            case 'Ort':
                self.model.addLocation(Location(name))
            case 'Fach':
                self.model.addSubject(Subject(name)) 
            case 'Objekt':
                self.model.addObject(Object(name))
            case 'Abteilung':
                self.model.addDepartment(Department(name))
            case 'Gruppe':
                self.model.addGroup(Group(name))
        self.model.save()
        self.masterDataDialog.hide()   

    def checkTable(self):
        self.page.fLocationTable.hide()
        self.page.fObjectTable.hide()
        self.page.fSubjectTable.hide()
        self.page.fDepartmentTable.hide()
        self.page.fGroupTable.hide()

        matchingText = self.page.fDropDownMenu.currentText()

        match matchingText:
            case 'Nutzer':
                self.page.fUserTable.show()
                self.databaseTable = matchingText
            case 'Ort':
                self.page.fLocationTable.show()
                self.databaseTable = matchingText
            case 'Objekt':
                self.page.fObjectTable.show()
                self.databaseTable = matchingText
            case 'Gruppe':
                self.page.fGroupTable.show()
                self.databaseTable = matchingText
            case 'Fach':
                self.page.fSubjectTable.show()
                self.databaseTable = matchingText
            case 'Abteilung':
                self.page.fDepartmentTable.show()
                self.databaseTable = matchingText
    def prepareObjectsForTable(self, objects: list[Object]):
        preparedObejcts = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObejcts.append(Object(name))
        return preparedObejcts
    def prepareLocationsForTable(self, objects: list[Location]):
        preparedObejcts = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObejcts.append(Location(name))
        return preparedObejcts
    def prepareSubjectsForTable(self, objects: list[Subject]):
        preparedObejcts = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObejcts.append(Subject(name))
        return preparedObejcts
    def prepareGroupsForTable(self, objects: list[Group]):
        preparedObejcts = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObejcts.append(Group(name))
        return preparedObejcts
    def prepareDepartmentsForTable(self, objects: list[Department]):
        preparedObejcts = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObejcts.append(Department(name))
        return preparedObejcts
    def refreshAll(self):
        self.model.load()
        self.objects = self.model.objects()
        self.subjects = self.model.subjects()
        self.locations = self.model.locations()
        self.departments = self.model.departments()
        self.groups = self.model.groups()
        match self.databaseTable:
            case 'Nutzer':
                self.currentTableItems = self.objects
            case 'Ort':
                self.currentTableItems = self.locations
            case 'Objekt':
                self.currentTableItems = self.objects
            case 'Gruppe':
                self.currentTableItems = self.groups
            case 'Fach':
                self.currentTableItems = self.subjects
            case 'Abteilung':
                self.currentTableItems = self.departments
        self.refreshTable()
    def refreshTable(self):
        match self.databaseTable:
            case 'Ort':
                preparedItems = self.prepareLocationsForTable(self.currentTableItems)
            case 'Objekt':
                preparedItems = self.prepareObjectsForTable(self.currentTableItems)
            case 'Gruppe':
                preparedItems = self.prepareGroupsForTable(self.currentTableItems)
            case 'Fach':
                preparedItems = self.prepareSubjectsForTable(self.currentTableItems)
            case 'Abteilung':
                preparedItems = self.prepareDepartmentsForTable(self.currentTableItems)
        self.refreshSpecialTableWithItems(preparedItems)
    def refreshSpecialTableWithItems(self, items: list[QTableWidgetItem]):
        self.page.fTable.setRowCount(len(items))
        for i in range(len(items)):
            self.page.fTable.setItem(i, 0, items[i].object)
            self.page.fTable.setCellWidget(i, 7, self.getDeleteButton(self.page.fTable))


