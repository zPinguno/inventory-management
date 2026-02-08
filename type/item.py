from type.itemstate import ItemState
from type.user import User


class Item:
    object: str
    group: str
    department: str
    subject: str
    location: str
    responsiblePerson: User
    borrowPerson: User
    state: ItemState

    def __init__(self,object, group,department, subject, location, responsiblePerson, borrowPerson, state):
        self.object = object
        self.group = group
        self.department = department
        self.subject = subject
        self.location = location 
        self.responsiblePerson = responsiblePerson
        self.borrowPerson = borrowPerson
        self.state = state
    def getobject(self): 
        return self.object
    def setobject(self, item): 
        self.object = item        
    def getGroup(self): 
        return self.group
    def setGroup(self, group): 
        self.group = group
    def getDepartment(self): 
        return self.department
    def setDepartment(self, department): 
        self.department = department
    def getSubject(self): 
        return self.subject
    def setSubject(self, subject): 
        self.subject = subject
    def getLocation(self):
        return self.location 
    def setLocation(self, location): 
        self.location = location
    def getResponsiblePerson(self):
        return self.responsiblePerson
    def setResponsiblePerson(self, responsiblePerson): 
        self.responsiblePerson = responsiblePerson
    def getBorrwoPerson(self):
        return self.borrowPerson
    def setBorrwoPerson(self, borrowPerson): 
        self.borrowPerson = borrowPerson