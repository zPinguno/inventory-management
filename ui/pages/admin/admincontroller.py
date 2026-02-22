from ui.pages.admin.adminpage import AdminPage
from ui.pages.pagecontrollerbase import PageControllerBase
from model.model import Model

class AdminController(PageControllerBase):
    page: AdminPage
    model: Model
    def __init__(self):
        super().__init__()
        self.page = AdminPage()
    def initLogic(self):
        pass