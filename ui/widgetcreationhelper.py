from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QMainWindow, QTableWidget, QComboBox, \
    QPushButton


def createButton(page:QMainWindow, name: str, layout:QVBoxLayout = None,  x=None, y=None):
    button = QPushButton(name, page)
    if x is not None and y is not None:
        button.move(x, y)
    if layout is not None:
        layout.addWidget(button)

    return button


def createDropDownMenu(page:QMainWindow, wordList: list, layout:QVBoxLayout):
    dropDownMenu = QComboBox(page)
    dropDownMenu.addItems(wordList)
    dropDownMenu.setEditable(True)
    dropDownMenu.lineEdit().setReadOnly(True)
    dropDownMenu.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
    dropDownMenu.setMinimumHeight(22)
    if layout is not None:
        layout.addWidget(dropDownMenu)

    return dropDownMenu
def createInput(page:QMainWindow, placeHolderName:str,layout:QVBoxLayout, x = None, y = None):
    lineEdit = QLineEdit(page)
    lineEdit.setPlaceholderText(placeHolderName)
    if x is not None and y is not None:
        lineEdit.move(x, y)
    if layout is not None:
        layout.addWidget(lineEdit)
    return lineEdit
def createText(name:str, layout:QVBoxLayout, x = None, y = None):
    label = QLabel(name)
    label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    if x is not None and y is not None:
        label.move(x, y)
    if layout is not None:
        layout.addWidget(label)
    return label
def createHeader(centerName:str, width: int, page:QMainWindow, x = None, y = None):
    layout = QVBoxLayout()
    headerWidget = QFrame(page)
    headerTitle = QLabel('<h2>' + centerName + '</h2>')
    headerTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    headerWidget.setFixedSize(width, 50) # Jeder der die Zahlen hier verändert ist eine Entäuschung
    headerWidget.setLayout(layout)
    layout.addWidget(headerTitle)
    if x is not None and y is not None:
        headerWidget.move(x, y)

    return headerWidget
def createSidepanel(page:QMainWindow):
    layout = QHBoxLayout()
    sidePanelWidget = QFrame(page)
    sidePanelWidget.setFixedSize(200, 600)
    sidePanelWidget.setLayout(layout)
    return sidePanelWidget


def createTitle(name:str,  layout:QVBoxLayout, x = None, y = None):
    label = QLabel('<h1>' + name + '</h1>')
    if x is not None and y is not None:
        label.move(x, y)
    if layout is not None:
        layout.addWidget(label, alignment= Qt.AlignmentFlag.AlignHCenter)

    return label
def createTable(page:QMainWindow, tableHeaders: list, x = None, y = None, width = None):
    table = QTableWidget(page)
    table.setColumnCount(len(tableHeaders))
    if width is not None:
        table.setFixedSize(width,550)
    else:
        table.setFixedSize(1000,550)
    table.resizeColumnToContents(len(tableHeaders))
    table.setHorizontalHeaderLabels(tableHeaders)
    table.horizontalHeader().setStyleSheet("QHeaderView::section { border: 1px solid gray; }")
    if x is not None and y is not None:
        table.move(x, y)


    return table