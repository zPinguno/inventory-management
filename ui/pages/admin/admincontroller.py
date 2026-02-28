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


