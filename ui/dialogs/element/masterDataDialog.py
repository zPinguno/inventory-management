from model.model import Model
from type.user import User
from type.userrole import UserRole
from ui.dialogs.dialogBase import DialogBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from type.itemheader import ItemHeader
from type.itemstate import ItemState
from typing import List

from ui.widgetcreationhelper import createCheckbox, createInput, createButton, createText


class MasterDataDialog(DialogBase):
    fVLayout: QVBoxLayout
    tableName: str 
    fNameInput: QLineEdit
    fSafeButton: QPushButton
    fCenterWidget: QWidget

    def __init__(self, tableName:str):
        self.tableName = tableName
        super().__init__()
        self.width = 140
        self.height = 100
        self.setWindowTitle("Eintrag erstellen")
        self.setFixedSize(self.width, self.height)


    def initComponents(self):
        super().initComponents()
        self.createWidgets()
        self.prepareWidgets()
        
    def createWidgets(self):
        self.fVLayout = QVBoxLayout()
        createText(f'Eintrag für {self.tableName}', self.fVLayout)
        self.fNameInput = createInput(self, 'Hier Eintippen', self.fVLayout)
        self.fSafeButton = createButton(self, 'Speichern', self.fVLayout)
        self.fCenterWidget = QWidget(self)


        self.prepareWidgets()
    def prepareWidgets(self):
        self.fCenterWidget.setLayout(self.fVLayout)
        self.fVLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)