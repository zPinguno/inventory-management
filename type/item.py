from type.itemstate import ItemState
from type.user import User
from type.object import Object
from type.group import Group
from type.department import Department
from type.subject import Subject
from type.location import Location

class Item:
    object: Object
    group: Group
    department: Department
    subject: Subject
    location: Location
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