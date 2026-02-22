from ui.dialogs.dialogBase import DialogBase

class DialogControllerBase:
    dialog: DialogBase
    def __init__(self):
        pass
    def showDialog(self):
        self.dialog.initComponents()
        self.initLogic()
    def hideDialog(self):
        self.dialog.hide()
    def initLogic(self):
        pass