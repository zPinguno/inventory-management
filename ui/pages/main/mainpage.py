from ui.pages.pageBase import PageBase
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

from ui.widgetcreationhelper import createInput, createTitle, createButton


class MainPage(PageBase):
    fVLayout: QVBoxLayout
    fLogoutButton: QPushButton
    fVLayout: QVBoxLayout
    def __init__(self):
        super().__init__()
    def initComponents(self):
        super().initComponents()
        self.loadStyleSheet()
        self.createWidgets()
        self.show()
    def createWidgets(self):
        self.fVLayout = QVBoxLayout()
        self.fLogoutButton = createInput(self, 'Logout', self.fVLayout)
    def loadStyleSheet(self):
        styleSheet = open('./ui/pages/main/main.css').read()
        self.setStyleSheet(styleSheet)