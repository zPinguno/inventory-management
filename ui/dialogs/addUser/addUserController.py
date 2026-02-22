from ui.dialogs.addUser.addUserDialog import AddUser
from ui.dialogs.dialogBaseController import DialogControllerBase
from model.model import Model

class AddUserController(DialogControllerBase):
    dialog: AddUser
    model: Model
    def __init__(self):
        super().__init__()
        self.dialog = AddUser()
    def initLogic(self):
        pass