from ui.pages.admin.adminpage import AdminPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class AdminController(PageControllerBase):
    page: AdminPage
    model: Model
    def __init__(self, selectPage):
        super().__init__(selectPage)
        self.page = AdminPage()
    def initLogic(self):
        self.checkTable()
        self.page.fDropDownMenu.currentIndexChanged.connect(self.checkTable)
        self.page.fSwitchSiteButton.clicked.connect(lambda: self.selectPage("Main"))

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
            case 'Ort':
                self.page.fLocationTable.show()
            case 'Objekt':
                self.page.fObjectTable.show()
            case 'Gruppe':
                self.page.fGroupTable.show()
            case 'Fach':
                self.page.fSubjectTable.show()
            case 'Abteilung':
                self.page.fDepartmentTable.show()
