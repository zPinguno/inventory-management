from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCheckBox, QLineEdit, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QMainWindow, QDialog, QTableWidget, QComboBox, \
    QPushButton, QWidget


def createButton(page:QMainWindow | QDialog, name: str, layout:QVBoxLayout = None,  x=None, y=None):
    button = QPushButton(name, page)
    checkForPosition(button, layout, x, y)

    return button

def createDropDownMenu(page:QMainWindow | QDialog, wordList: list, layout:QVBoxLayout = None, x = 0, y = 0):
    dropDownMenu = QComboBox(page)
    dropDownMenu.addItems(wordList)
    dropDownMenu.setEditable(True)
    dropDownMenu.lineEdit().setReadOnly(True)
    dropDownMenu.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
    dropDownMenu.setMinimumHeight(22)
    checkForPosition(dropDownMenu, layout, x, y)

    return dropDownMenu
def createInput(page:QMainWindow | QDialog , placeHolderName:str,layout:QVBoxLayout, x = None, y = None):
    lineEdit = QLineEdit(page)
    lineEdit.setPlaceholderText(placeHolderName)

    checkForPosition(lineEdit, layout, x, y)

    return lineEdit
def createCheckbox(page:QMainWindow | QDialog , name:str,layout:QVBoxLayout, x = None, y = None):
    checkBox = QCheckBox(name, page)
    checkForPosition(checkBox, layout, x, y)

    return checkBox

def createText(name:str, layout:QVBoxLayout, x = None, y = None):
    label = QLabel(name)
    label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    checkForPosition(label, layout, x, y)

    return label
def createHeader(centerName:str, width: int, page:QMainWindow | QDialog, x = None, y = None):
    layout = QVBoxLayout()
    headerWidget = QFrame(page)
    headerTitle = QLabel('<h2>' + centerName + '</h2>')
    headerTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    headerWidget.setFixedSize(width, 50) # Jeder der die Zahlen hier verändert ist eine Entäuschung
    checkForPosition(headerWidget, layout, x, y)

    return headerWidget
def createSidepanel(page:QMainWindow | QDialog):
    layout = QHBoxLayout()
    sidePanelWidget = QFrame(page)
    sidePanelWidget.setFixedSize(200, 600)
    sidePanelWidget.setLayout(layout)
    return sidePanelWidget


def createTitle(name:str,  layout:QVBoxLayout, x = None, y = None):
    label = QLabel('<h1>' + name + '</h1>')
    label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    checkForPosition(label, layout, x, y)

    return label
def createTable(page:QMainWindow | QDialog, tableHeaders: list, x = None, y = None, width = None):
    table = QTableWidget(page)
    table.setColumnCount(len(tableHeaders))
    if width is not None:
        table.setFixedSize(width,550)
    else:
        table.setFixedSize(1000,550)
    table.resizeColumnToContents(len(tableHeaders))
    table.setHorizontalHeaderLabels(tableHeaders)
    table.horizontalHeader().setStyleSheet("QHeaderView::section { border: 1px solid gray; }")
    checkForPosition(table, None, x, y)


    return table

def checkForPosition(widget: QWidget, layout: QVBoxLayout = None, x = None, y = None):
    if x is not None and y is not None:
        widget.move(x, y)
    if layout is not None:
        layout.addWidget(widget)