from model.model import Model
from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *

from ui.widgetcreationhelper import createTable, createButton, createHeader, createDropDownMenu


class AdminPage(PageBase):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel: QFrame
    fUserTable: QTableWidget
    fLocationTable: QTableWidget
    fObjectTable: QTableWidget
    fSubjectTable: QTableWidget
    fGroupTable: QTableWidget
    fDepartmentTable: QTableWidget
    fDropDownMenu: QComboBox
    fNewEntryButton: QPushButton
    fHeaderAdminButton: QPushButton
    fAddItemButton: QPushButton
    fRemoveItemButton: QPushButton
    def __init__(self):
        super().__init__()
    def initComponents(self):
        super().initComponents()
        self.setWindowTitle('main')
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fHeaderButton = createButton(self, 'Logout', x = 850, y = 6)
        self.fSwitchSiteButton = createButton(self, 'Inventar Seite', x=15, y=6)
        self.fDropDownMenu = createDropDownMenu(self, ['Nutzer', 'Gruppe', 'Ort', 'Fach', 'Objekt', 'Abteilung'], x = 500, y = 6)
        self.fUserTable = createTable(self, ['Vorname', 'Nachname', 'Nutzername', 'Rolle', 'Löschen'],x = 0, y = 50)
        self.fLocationTable = createTable(self, ['Name','Löschen'],x = 0, y = 50)
        self.fSubjectTable = createTable(self, ['Name','Löschen'],x = 0, y = 50)
        self.fObjectTable = createTable(self, ['Name','Löschen'],x = 0, y = 50)
        self.fGroupTable = createTable(self, ['Name','Löschen'],x = 0, y = 50)
        self.fDepartmentTable = createTable(self, ['Name','Löschen'],x = 0, y = 50)
        self.fHeader = createHeader(
        'Admin Seite',
        1000,
        self 
        )
        self.fAddItemButton = createButton(self,'+', x = self.width - 80, y = self.height - 80)
        self.prepareWidgets()
    def prepareWidgets(self):
        self.fAddItemButton.setFixedSize(60, 60)

        self.fUserTable.move(500, 50)
        self.fLocationTable.move(500, 50)
        self.fSubjectTable.move(500, 50)
        self.fObjectTable.move(500, 50)
        self.fGroupTable.move(500, 50)
        self.fDepartmentTable.move(500, 50)


        self.fHeaderButton.raise_()
        self.fDropDownMenu.raise_()
        self.fSwitchSiteButton.raise_()

    def prepareStyles(self):
        pass # Ehrlich, keine Ahnung für Styles

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/admin/admin.css').read()
        self.setStyleSheet(styleSheet)