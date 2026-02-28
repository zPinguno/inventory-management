from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QLabel, QPushButton, QWidget

from model.model import Model
from type.department import Department
from type.group import Group
from type.item import Item
from type.itemstate import getAllStates, getAllStatesAsText, normalizeText
from type.location import Location
from type.object import Object
from type.subject import Subject
from type.user import User
from ui.dialogs.dialogBase import DialogBase
from ui.widgetcreationhelper import createText, createButton, createDropDownMenu


class AddItem(DialogBase):
    model: Model

    fVLayout: QVBoxLayout
    fCenterWidget: QWidget

    fObjectDropdown: QComboBox
    fGroupDropdown: QComboBox
    fDepartmentDropdown: QComboBox
    fSubjectDropdown: QComboBox
    fLocationDropdown: QComboBox
    fResponsiblePersonDropdown: QComboBox
    fStateDropdown: QComboBox

    fObjectLabel: QLabel
    fGroupLabel: QLabel
    fDepartmentLabel: QLabel
    fSubjectLabel: QLabel
    fLocationLabel: QLabel
    fResponsiblePersonLabel: QLabel
    fStateLabel: QLabel

    fSaveButton: QPushButton
    def __init__(self, model:Model):
        self.model = model
        super().__init__()

    def initComponents(self):
        super().initComponents()
        self.createWidgets()
        self.refreshWordlist(self.model)

    def createWidgets(self):
        self.fVLayout = QVBoxLayout()

        self.fObjectLabel = createText('Itemname', self.fVLayout)
        self.fObjectDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fGroupLabel = createText('Gruppe', self.fVLayout)
        self.fGroupDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fDepartmentLabel = createText('Abteilung', self.fVLayout)
        self.fDepartmentDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fSubjectLabel = createText('Fach', self.fVLayout)
        self.fSubjectDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fLocationLabel = createText('Ort', self.fVLayout)
        self.fLocationDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fResponsiblePersonLabel = createText('Verantwortlicher', self.fVLayout)
        self.fResponsiblePersonDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fStateLabel = createText('Zustand', self.fVLayout)
        self.fStateDropdown = createDropDownMenu(self, list(), self.fVLayout)

        self.fSaveButton = createButton(self, 'Speichern', self.fVLayout)

        self.fCenterWidget = QWidget(self)
        self.fCenterWidget.setLayout(self.fVLayout)

    def refreshWordlist(self, model:Model):
        model.load()
        self.fObjectDropdown.clear()
        self.fObjectDropdown.addItems(model.getAllObjects())
        self.fGroupDropdown.clear()
        self.fGroupDropdown.addItems(model.getAllGroups())
        self.fDepartmentDropdown.clear()
        self.fDepartmentDropdown.addItems(model.getAllDepartments())
        self.fSubjectDropdown.clear()
        self.fSubjectDropdown.addItems(model.getAllSubjects())
        self.fLocationDropdown.clear()
        self.fLocationDropdown.addItems(model.getAllLocations())
        self.fResponsiblePersonDropdown.clear()
        self.fResponsiblePersonDropdown.addItems(model.getAllResponsibleUser())
        self.fStateDropdown.clear()
        self.fStateDropdown.addItems(getAllStatesAsText())

    def getResult(self):
        object = self.getInstanceByText(self.fObjectDropdown.currentText(), Object)
        group = self.getInstanceByText(self.fGroupDropdown.currentText(), Group)
        department = self.getInstanceByText(self.fDepartmentDropdown.currentText(), Department)
        subject = self.getInstanceByText(self.fSubjectDropdown.currentText(), Subject)
        location = self.getInstanceByText(self.fLocationDropdown.currentText(), Location)
        state = normalizeText(self.fStateDropdown.currentText())
        responsiblePerson = self.model.getUserByUserName(self.fResponsiblePersonDropdown.currentText())
        item = Item(object, group, department, subject, location, responsiblePerson, state)

        return item
    def getInstanceByText(self, text:str, type):
        return type(text)