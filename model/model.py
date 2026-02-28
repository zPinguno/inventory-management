import sqlite3
import json
from typing import List

from type.itemstate import normalizeItems, normalizeText, ItemState
from type.user import User
from type.item import Item
from type.userrole import UserRole, normalizeRoleText
from type.object import Object
from type.department import Department
from type.subject import Subject
from type.group import Group
from type.location import Location
from type.itemheader import ItemHeader


class Model:
    def __init__(self, db_path: str = "local.db"):
        self.db_path = db_path
        self.users: List[User] = []
        self.items: List[Item] = []
        self.objects: List[Object] = []
        self.departments: List[Department] = []
        self.locations: List[Location] = []
        self.subjects: List[Subject] = []
        self.groups: List[Group] = list()
        self.load()

    def _ensure_tables(self, conn: sqlite3.Connection) -> None:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            LastName TEXT,
            UserName TEXT UNIQUE,
            Password TEXT,
            Role TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            itemName TEXT,
            GroupName TEXT,
            Department TEXT,
            Subject TEXT,
            Location TEXT,
            ResponsiblePerson TEXT,
            State TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Subjects (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Groups (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Objects (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Locations (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.commit()

    def save(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)
            conn.execute("DELETE FROM Users")
            if self.users:
                conn.executemany(
                    "INSERT INTO Users (FirstName, LastName, UserName, Password, Role) VALUES (?, ?, ?, ?, ?)",
                    ((u.firstName, u.lastName, u.userName, u.password, json.dumps([e.value for e in u.roles])) for u in self.users)
                )

            conn.execute("DELETE FROM Items")
            if self.items:
                conn.executemany(
                    "INSERT INTO Items (itemName, GroupName, Department, Subject, Location, ResponsiblePerson, State) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    ((i.object.getName(), i.group.getName(), i.department.getName(), i.subject.getName(), i.location.getName(), i.responsiblePerson.userName if isinstance(i.responsiblePerson, User) else i.responsiblePerson, i.state.value if hasattr(i.state, 'value') else i.state) for i in self.items)
                    )

            conn.execute("DELETE FROM Departments")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Departments (Name) VALUES (?)",
                    ((u.getName(),) for u in self.departments)
                )
            conn.execute("DELETE FROM Subjects")
            if self.subjects:
                conn.executemany(
                    "INSERT INTO Subjects (Name) VALUES (?)",
                    ((u.getName(),) for u in self.subjects)
                )
            conn.execute("DELETE FROM Groups")
            if self.groups:
                conn.executemany(
                    "INSERT INTO Groups (Name) VALUES (?)",
                    ((u.getName(),) for u in self.groups)
                )
            conn.execute("DELETE FROM Objects")
            if self.objects:
                conn.executemany(
                    "INSERT INTO Objects (Name) VALUES (?)",
                    ((u.getName(),) for u in self.objects)
                )
            conn.execute("DELETE FROM Locations")
            if self.locations:
                conn.executemany(
                    "INSERT INTO Locations (Name) VALUES (?)",
                    ((u.getName(),) for u in self.locations)
                )
    def load(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)

            cur = conn.execute("SELECT FirstName, LastName, UserName, Password, Role FROM Users ORDER BY Id")
            users = [
                User(
                    firstName=row[0] or "",
                    lastName=row[1] or "",
                    userName=row[2] or "",
                    password=row[3] or "",
                    roles= json.loads(row[4]) or ""
                )
                for row in cur.fetchall()
            ]
            self.users = self.normalizeUsers(users)

            cur = conn.execute("SELECT itemName, GroupName, Department, Subject, Location, ResponsiblePerson, State FROM Items ORDER BY Id")
            self.items = normalizeItems([
                Item(obj=Object(row[0]), group=Group(row[1]), department=Department(row[2]), subject=Subject(row[3]), location=Location(row[4]), responsiblePerson=self.getUserByUserName(row[5]), state=ItemState(row[6]))
                for row in cur.fetchall()
            ])
            cur = conn.execute("SELECT Name FROM Groups ORDER BY Id")
            self.groups = [
                Group(name=row[0]) for row in cur.fetchall()
            ]
            cur = conn.execute("SELECT Name FROM Objects ORDER BY Id")
            self.objects = [
                Object(name=row[0]) for row in cur.fetchall()
            ]
            cur = conn.execute("SELECT Name FROM Subjects ORDER BY Id")
            self.subjects = [
                Subject(name=row[0]) for row in cur.fetchall()
            ]
            cur = conn.execute("SELECT Name FROM Departments ORDER BY Id")
            self.departments = [
                Department(name=row[0]) for row in cur.fetchall()
            ]
            cur = conn.execute("SELECT Name FROM Locations ORDER BY Id")
            self.locations = [
                Location(name=row[0]) for row in cur.fetchall()
            ]
    def normalizeUsers(self, users: List[User]):
        for user in users:
            roles = list[UserRole]()
            for role in user.roles:
                roles.append(normalizeRoleText(role))
            user.setRoles(roles)
        return users

    def addUser(self, user: User) -> None:
        self.users.append(user)

    def addItem(self, item: Item) -> None:
        self.items.append(item)

    def addDepartment(self, department: Department) -> None:
        self.departments.append(department)

    def addObject(self, object: Object) -> None:
        self.objects.append(object)
    
    def addSubject(self, subject: Subject) -> None:
        self.subjects.append(subject)
        
    def addGroup(self, group: Group) -> None:
        self.groups.append(group)
    
    def addLocation(self, location: Location) -> None:
        self.locations.append(location)
    
    def login(self, userName: str, password: str) -> User | None:
        for u in self.users:
            if u.userName == userName and u.password == password:
                return u
        return None
    
    def getAllResponsibleUser(self):
        responsibilUser = []
        for user in self.users:
            if UserRole.RESPONSIBLE in user.roles:
                responsibilUser.append(user)
        return responsibilUser
    def getAllResponsibleUserNames(self):
        responsibilUser = []
        for user in self.users:
            if UserRole.RESPONSIBLE in user.roles:
                responsibilUser.append(user.userName)
        return responsibilUser

    def getUserByUserName(self, userName: str):
        searchedUser = None
        for user in self.users:
            if userName in user.userName:
                searchedUser = user
        return searchedUser
    
    def getAllDepartments(self): 
        return self.departments
    
    def getAllSubjects(self):     
        return self.subjects
    
    def getAllObjects(self): 
        return self.objects
        
    def getAllLocations(self): 
        return self.locations
    
    def getAllGroups(self): 
        return self.groups