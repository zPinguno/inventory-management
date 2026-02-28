from PyQt6.QtWidgets import QMainWindow, QPushButton


class PageBase(QMainWindow):
    fSwitchSiteButton: QPushButton

    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.setFixedSize(self.width, self.height)

    def initComponents(self):
        pass
    def deInitComponents(self):
        pass