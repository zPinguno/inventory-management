import sys
from PyQt6.QtWidgets import QApplication
from ui.controller import Controller

sys.path.append(".")
app = QApplication(sys.argv)
controller = Controller()

sys.exit(app.exec())
