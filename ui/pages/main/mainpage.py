from model.model import Model
from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from type.itemheader import ItemHeader
from type.itemstate import ItemState

from ui.widgetcreationhelper import createDropDownMenu, createInput, createTable, createButton, createSidepanel, createHeader, createText


class MainPage(PageBase):
    model: Model
    fTitle: QLabel
    fHeader: QFrame
    fLogoutButton: QPushButton
    fExportButton: QPushButton
    fTable: QTableWidget
    fAddItemButton: QPushButton
    fFilterDropDown: QComboBox
    fFilterInput: QLineEdit
    fFilterSearchButton: QPushButton
    fFilterResetButton: QPushButton
    fStateDropDown: QComboBox
    fResponsiblePersonDropDown: QComboBox
    fFilterWidget = QWidget
    fVLayout = QVBoxLayout
    fFilterLabel = QLabel
    fMainFilterWidget = QWidget
    fFilterSelected = ''
    tableHeaders = [ItemHeader.OBJECT.value ,ItemHeader.GROUP.value, ItemHeader.DEPARTMENT.value, ItemHeader.SUBJECT.value, ItemHeader.LOCATION.value, ItemHeader.RESPONSIBLE.value, ItemHeader.STATE.value, 'Löschen']
    filterHeaders = [ItemHeader.OBJECT.value, ItemHeader.GROUP.value, ItemHeader.DEPARTMENT.value, ItemHeader.SUBJECT.value, ItemHeader.LOCATION.value, ItemHeader.RESPONSIBLE.value, ItemHeader.STATE.value]
    def __init__(self,model):
        self.model = model
        super().__init__()
    def initComponents(self):
        super().initComponents()
        self.setWindowTitle('Main')
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fLogoutButton = createButton(self, 'Logout', x = 850, y = 6)
        self.fSwitchSiteButton = createButton(self, 'Admin Seite', x = 15, y = 6)
        self.fExportButton = createButton(self, 'Export in CSV', x = 250, y = 6)
        self.fAddItemButton = createButton(self, '+', x = self.width - 80, y = self.height - 80)
  
        self.fVLayout = QVBoxLayout()
        distanceSidePanel = 200

        self.fTable = createTable(self, self.tableHeaders ,x = distanceSidePanel, y = 50, width = 850)
        self.fHeader = createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        page= self,
        x = distanceSidePanel, y = 0
        )
    
        self.fFilterLabel = createText('Suche:', self.fVLayout)
        self.fFilterDropDown = createDropDownMenu(self, self.filterHeaders, self.fVLayout)

        stateList = [state.value for state in ItemState]
        self.fStateDropDown = createDropDownMenu(self, stateList, self.fVLayout)
        self.fFilterInput = createInput(self, 'Hier eingeben.', self.fVLayout)
        allResponsibles = self.model.getAllResponsibleUser()
        responsibleList = list()
        for user in allResponsibles:
            responsibleList.append(user.userName)
        self.fResponsiblePersonDropDown = createDropDownMenu(self, responsibleList, self.fVLayout)
        self.fFilterSearchButton = createButton(self, 'Suchen', self.fVLayout )
        self.fFilterResetButton = createButton(self, 'Filter Zurücksetzen', self.fVLayout)
        self.fMainFilterWidget = QWidget(self)

        self.prepareWidgets()
    def prepareWidgets(self):
        self.fTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fMainFilterWidget.move(0, 200)
        self.fMainFilterWidget.setLayout(self.fVLayout)
        self.fMainFilterWidget.setFixedSize(200, 130)
        self.fVLayout.setSpacing(5)
        self.fAddItemButton.setFixedSize(60, 60)

        self.fSwitchSiteButton.raise_()
        self.fLogoutButton.raise_()
        self.fExportButton.raise_()
        self.fAddItemButton.raise_()
    def prepareStyles(self):
        self.fMainFilterWidget.setProperty('id', 'filterLabelElement')
        self.fFilterSearchButton.setProperty('id', 'filterSearchbuttonElement')
        

    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/main/main.css').read()
        self.setStyleSheet(styleSheet)