from PyQt6.QtWidgets import QMessageBox, QPushButton, QTableWidgetItem
from type.user import User
from type.userrole import UserRole
from ui.dialogs.addUser.addUserDialog import AddUser
from ui.dialogs.element.masterDataDialog import MasterDataDialog
from ui.pages.admin.adminpage import AdminPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model
from type.location import Location
from type.subject import Subject
from type.group import Group
from type.object import Object
from type.department import Department
from type.tableuser import TableItem as TableUser
from helper.Helper import hashPassword

class AdminController(PageControllerBase):
    page: AdminPage
    users: list[User]
    models: list[Model]
    objects: list[Object]
    subjects: list[Subject]
    locations: list[Location]
    departments: list[Department]
    groups: list[Group]
    masterDataDialog: MasterDataDialog
    addUserDialog: AddUser
    databaseTable: str
    def __init__(self, selectPage):
        super().__init__(selectPage, None)
        self.page = AdminPage()
        self.model = Model()
    def initLogic(self):
        super().initLogic()
        self.checkTable()
        self.refreshAll()

        self.page.fDropDownMenu.currentIndexChanged.connect(self.checkTable)
        self.page.fDropDownMenu.currentIndexChanged.connect(self.refreshAll)
        
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Main"))
        self.page.fAddItemButton.clicked.connect(self.selectDialog)

    def selectDialog(self):
        if (self.databaseTable == 'Nutzer'):
            self.showAddUserDialog()
        else:
            self.showMasterDataDialog()
    def showMasterDataDialog(self):
        self.masterDataDialog = MasterDataDialog(self.databaseTable)
        self.masterDataDialog.show()
        self.masterDataDialog.fSaveButton.clicked.connect(self.safeMasterDataEntry)

    def showAddUserDialog(self):
        self.addUserDialog = AddUser()
        self.addUserDialog.show()
        self.addUserDialog.fSaveButton.clicked.connect(self.safeUserEntry)
    
    def safeMasterDataEntry(self):
        if self.masterDataDialog.fNameInput.text() == "":
            self.showDialogError(self.masterDataDialog)
            return
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
        self.refreshAll()
    def safeUserEntry(self):
            firstName = self.addUserDialog.fFirstNameInput.text()
            lastName = self.addUserDialog.fLastNameInput.text()
            userName = self.addUserDialog.fUserNameInput.text()
            password = self.addUserDialog.fPasswordInput.text()
            roles = []
            if self.addUserDialog.fAdminCheckbox.isChecked():
                roles.append(UserRole.ADMIN)
            if self.addUserDialog.fResponsiblePersonCheckbox.isChecked():
                roles.append(UserRole.RESPONSIBLE)
            if self.addUserDialog.fTeacherCheckbox.isChecked():
                roles.append(UserRole.TEACHER)

            if firstName == "" or lastName == "" or userName == "" or password == "" or len(roles) == 0:
                self.showDialogError(self.addUserDialog)
                return
            newUser = User(firstName, lastName, userName, hashPassword(password), roles)
            self.model.addUser(newUser)
            self.model.save()
            self.addUserDialog.hide()
            self.refreshAll()

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
    def prepareUsersForTable(self, users: list[User]):
        preparedUsers = list()
        for user in users:
            firstName = QTableWidgetItem(user.firstName)
            lastName = QTableWidgetItem(user.lastName)
            username = QTableWidgetItem(user.userName)
            userType = QTableWidgetItem(", ".join([role.value for role in user.roles]))
            preparedUsers.append(TableUser(firstName, lastName, username, userType))
        return preparedUsers
    def prepareObjectsForTable(self, objects: list[Object]):
        preparedObjects = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObjects.append(Object(name))
        return preparedObjects
    def prepareLocationsForTable(self, objects: list[Location]):
        preparedLocations = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedLocations.append(Location(name))
        return preparedLocations
    def prepareSubjectsForTable(self, objects: list[Subject]):
        preparedSubjects = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedSubjects.append(Subject(name))
        return preparedSubjects
    def prepareGroupsForTable(self, objects: list[Group]):
        preparedGroups = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedGroups.append(Group(name))
        return preparedGroups
    def prepareDepartmentsForTable(self, objects: list[Department]):
        preparedObjects = list()
        for object in objects:
            name = QTableWidgetItem(object.getName())
            preparedObjects.append(Department(name))
        return preparedObjects
    
    def refreshAll(self):
        self.model.load()
        self.users = self.model.users
        self.objects = self.model.objects
        self.subjects = self.model.subjects
        self.locations = self.model.locations
        self.departments = self.model.departments
        self.groups = self.model.groups
        match self.databaseTable:
            case 'Nutzer':
                self.currentTableItems = self.users
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
            case 'Nutzer':
                preparedItems = self.prepareUsersForTable(self.currentTableItems)
                self.refreshTableWithUsers(preparedItems)
                return
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
        currenTable = self.getCurrentTable()
        currenTable.setRowCount(len(items))
        for i in range(len(items)):
            currenTable.setItem(i, 0, items[i].getName())
            currenTable.setCellWidget(i, 1, self.getDeleteButton(currenTable))
    def refreshTableWithUsers(self, items: list[QTableWidgetItem]):
        currenTable = self.getCurrentTable()
        currenTable.setRowCount(len(items))
        for i in range(len(items)):
            currenTable.setItem(i, 0, items[i].firstname)
            currenTable.setItem(i, 1, items[i].lastname)
            currenTable.setItem(i, 2, items[i].userName)
            currenTable.setItem(i, 3, items[i].usertype)
            currenTable.setCellWidget(i, 4, self.getDeleteButton(currenTable))
    def getCurrentTable(self):
        match self.databaseTable:
            case 'Nutzer':
                return self.page.fUserTable
            case 'Ort':
                return self.page.fLocationTable
            case 'Objekt':
                return self.page.fObjectTable
            case 'Gruppe':
                return self.page.fGroupTable
            case 'Fach':
                return self.page.fSubjectTable
            case 'Abteilung':
                return self.page.fDepartmentTable
    def getDeleteButton(self,table):
        deleteButton = QPushButton("Löschen")
        deleteButton.clicked.connect(lambda: self.removeItemRowAtButton(deleteButton, table))

        return deleteButton
    def removeItemRowAtButton(self, deleteButton, table):
        if deleteButton:
            index = table.indexAt(deleteButton.pos())
            if index.isValid():
                table.removeRow(index.row())
                match self.databaseTable:
                    case 'Nutzer':
                        self.model.users.pop(index.row())   
                    case 'Ort':
                        self.model.locations.pop(index.row())
                    case 'Objekt':
                        self.model.objects.pop(index.row())
                    case 'Gruppe':
                        self.model.groups.pop(index.row())
                    case 'Fach':
                        self.model.subjects.pop(index.row())
                    case 'Abteilung':
                        self.model.departments.pop(index.row())
                self.model.save()
        self.refreshAll()


    def showDialogError(self, dialog):
        errorDialog = QMessageBox(dialog)
        errorDialog.setIcon(QMessageBox.Icon.Warning)
        errorDialog.setWindowTitle('Eintrag Fehler')
        errorDialog.setText('Alle Felder müssen ausgefüllt werden!')
        errorDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        errorDialog.exec()