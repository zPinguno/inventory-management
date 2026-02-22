from model.model import Model
from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *

from ui.widgetcreationhelper import createTable, createButton, createHeader


class AdminPage(PageBase):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel: QFrame
    fHeaderButton: QPushButton
    fTable: QTableWidget
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
        self.fHeaderAdminButton = createButton(self, 'Stammdaten ändern', x = 450, y = 6)
        self.fTable = createTable(self, ['Vorname', 'Nachname', 'Nutzername', 'Rolle', 'Löschen'],x = 0, y = 50)
        self.fHeader = createHeader(
        'Admin Seite',
        1000,
        self 
        )
        self.fAddItemButton = createButton(self,'+', x = self.width - 80, y = self.height - 80)
        self.prepareWidgets()
    def prepareWidgets(self):
        self.fHeaderButton.raise_()
        self.fAddItemButton.setFixedSize(60, 60)
    def prepareStyles(self):
        pass # Ehrlich, keine Ahnung für Styles

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/admin/admin.css').read()
        self.setStyleSheet(styleSheet)