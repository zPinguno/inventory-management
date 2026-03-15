from model.model import Model
from type.object import Object
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
    fLogoutButton: QPushButton
    def __init__(self):
        super().__init__()
    def initComponents(self):
        super().initComponents()
        self.setWindowTitle('main')
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fLogoutButton = createButton(self, 'Logout', x = 850, y = 6)
        self.fSwitchSiteButton = createButton(self, 'Inventar Seite', x = 5, y = 10)
        self.fDropDownMenu = createDropDownMenu(self, ['Ort', 'Nutzer', 'Gruppe', 'Fach', 'Objekt', 'Abteilung'], x = 420, y = 6)
        self.fUserTable = createTable(self, ['Vorname', 'Nachname', 'Nutzername', 'Rolle', 'Löschen'],x = 180, y = 50, width = 850)
        self.fLocationTable = createTable(self, ['Name','Löschen'],x = 180, y = 50, width = 850)
        self.fSubjectTable = createTable(self, ['Name','Löschen'],x = 180, y = 50, width = 850)
        self.fObjectTable = createTable(self, ['Name','Löschen'],x = 180, y = 50, width = 850)
        self.fGroupTable = createTable(self, ['Name','Löschen'],x = 180, y = 50, width = 850)
        self.fDepartmentTable = createTable(self, ['Name','Löschen'],x = 180, y = 50, width = 850)
        self.fHeader = createHeader(
        'Admin Seite',
        1000,
        self 
        )
        self.fAddItemButton = createButton(self,'+', x = self.width - 80, y = self.height - 80)
        self.prepareWidgets()
    def prepareWidgets(self):
        self.fAddItemButton.setFixedSize(60, 60)
        self.fUserTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fLocationTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fObjectTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fSubjectTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fGroupTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fDepartmentTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


        self.fLogoutButton.raise_()
        self.fDropDownMenu.raise_()
        self.fSwitchSiteButton.raise_()

    def prepareStyles(self):
        pass # Ehrlich, keine Ahnung für Styles

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/admin/admin.css').read()
        self.setStyleSheet(styleSheet)