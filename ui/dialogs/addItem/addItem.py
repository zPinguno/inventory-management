from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QLabel, QPushButton, QWidget, QDialog

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
    item: Item

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
    def __init__(self, model:Model, getBaseDataAsStrings, item:Item = None):
        QDialog.__init__(self)
        self.getBaseDataAsStrings = getBaseDataAsStrings
        self.model = model
        self.item = item
        self.width = 400
        self.height = 400
        self.setFixedSize(self.width, self.height)
        # initComponents explicitly called here instead of in DialogBase constructor
        self.initComponents()

    def selectWindowTitle(self):
        if self.item is not None:
            self.setWindowTitle("Eintrag bearbeiten")
        else:
            self.setWindowTitle("Eintrag erstellen")

    def initComponents(self):
        super().initComponents()
        self.setHeight()
        self.selectWindowTitle()
        self.createWidgets()
        self.refreshWordlist(self.model)
        self.prefillWidgets()

    def setHeight(self):
        self.width = 195
        self.height = 450
        self.setFixedSize(self.width, self.height)

    def createWidgets(self):
        self.fVLayout = QVBoxLayout()

        self.fObjectLabel = createText('Name', self.fVLayout)
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

    def prefillWidgets(self):
        if self.item is None:
            return
        self.fObjectDropdown.setCurrentText(self.item.object.getName())
        self.fGroupDropdown.setCurrentText(self.item.group.getName())
        self.fDepartmentDropdown.setCurrentText(self.item.department.getName())
        self.fSubjectDropdown.setCurrentText(self.item.subject.getName())
        self.fLocationDropdown.setCurrentText(self.item.location.getName())
        self.fResponsiblePersonDropdown.setCurrentText(self.item.responsiblePerson.userName)
        self.fStateDropdown.setCurrentText(self.item.state.value)
        self.fSaveButton.setText('Speichern')

    def refreshWordlist(self, model:Model):
        model.load()
        self.fObjectDropdown.clear()
        self.fObjectDropdown.addItems(self.getBaseDataAsStrings(model.getAllObjects()))
        self.fGroupDropdown.clear()
        self.fGroupDropdown.addItems(self.getBaseDataAsStrings(model.getAllGroups()))
        self.fDepartmentDropdown.clear()
        self.fDepartmentDropdown.addItems(self.getBaseDataAsStrings(model.getAllDepartments()))
        self.fSubjectDropdown.clear()
        self.fSubjectDropdown.addItems(self.getBaseDataAsStrings(model.getAllSubjects()))
        self.fLocationDropdown.clear()
        self.fLocationDropdown.addItems(self.getBaseDataAsStrings(model.getAllLocations()))
        self.fResponsiblePersonDropdown.clear()
        self.fResponsiblePersonDropdown.addItems(self.getResponsibleUsernames(model))
        self.fStateDropdown.clear()
        self.fStateDropdown.addItems(getAllStatesAsText())

    def getResponsibleUsernames(self, model:Model):
        allResponsibles = model.getAllResponsibleUser()
        responsibleList = list()
        for user in allResponsibles:
            responsibleList.append(user.userName)
        return responsibleList

    def getResult(self):
        object = self.model.findBaseDataByName(self.model.getAllObjects(), self.fObjectDropdown.currentText())
        group = self.model.findBaseDataByName(self.model.getAllGroups(), self.fGroupDropdown.currentText())
        department = self.model.findBaseDataByName(self.model.getAllDepartments(), self.fDepartmentDropdown.currentText())
        subject = self.model.findBaseDataByName(self.model.getAllSubjects(), self.fSubjectDropdown.currentText())
        location = self.model.findBaseDataByName(self.model.getAllLocations(), self.fLocationDropdown.currentText())
        state = normalizeText(self.fStateDropdown.currentText())
        responsiblePerson = self.model.getUserByUserName(self.fResponsiblePersonDropdown.currentText())

        return Item(object, group, department, subject, location, responsiblePerson, state)

    def getInstanceByText(self, text:str, type):
        return type(text)