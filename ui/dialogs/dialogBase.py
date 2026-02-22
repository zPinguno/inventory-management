from PyQt6.QtWidgets import QDialog


class DialogBase(QDialog):
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 400
        self.setFixedSize(self.width, self.height)

    def initComponents(self):
        pass