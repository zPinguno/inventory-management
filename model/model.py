import sqlite3
from typing import List

from type.itemstate import normalizeItems
from type.user import User
from type.item import Item
from type.userrole import normalizeUsers, UserRole
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
        self.groups: List[Group] = []
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
            BorrowPerson TEXT,
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
                    ((u.firstName, u.lastName, u.userName, u.password, u.roles.value if isinstance(u.roles, UserRole) else u.roles) for u in self.users)
                )

            conn.execute("DELETE FROM Items")
            if self.items:
                conn.executemany(
                    "INSERT INTO Items (GroupName, Department, Subject, Location, ResponsiblePerson, State) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    ((i.object, i.group, i.department, i.subject, i.location, i.responsiblePerson.userName if isinstance(i.responsiblePerson, User) else i.responsiblePerson, i.borrowPerson.userName if isinstance(i.responsiblePerson, User) else i.responsiblePerson, i.state.value if hasattr(i.state, 'value') else i.state) for i in self.items)
                )

            conn.execute("DELETE FROM Departments")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Departments (Name) VALUES (?)",
                    ((u.name) for u in self.departments)
                )
            conn.execute("DELETE FROM Subjects")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Subjects (Name) VALUES (?)",
                    ((u.name) for u in self.subjects)
                )
            conn.execute("DELETE FROM Groups")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Groups (Name) VALUES (?)",
                    ((u.name) for u in self.groups)
                )
    def load(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)

            cur = conn.execute("SELECT FirstName, LastName, UserName, Password, Role FROM Users ORDER BY Id")
            self.users = normalizeUsers([
                User(
                    firstName=row[0] or "",
                    lastName=row[1] or "",
                    userName=row[2] or "",
                    password=row[3] or "",
                    roles=row[4] or ""
                )
                for row in cur.fetchall()
            ])

            cur = conn.execute("SELECT GroupName, Department, Subject, Location, ResponsiblePerson, State FROM Items ORDER BY Id")
            self.items = normalizeItems([
                Item(group=row[0], department=row[1], subject=row[2], location=row[3], responsiblePerson=row[4], state=row[5] )
                for row in cur.fetchall()
            ])


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

    def getAllUserNamesByRole(self, userRole = UserRole.ADMIN.value or UserRole.BORROWER.value or
        UserRole.RESPONSIBLE.value or UserRole.TEACHER.value):
        self.load()
        users = self.users
        responsibilityUserNames = []
        for user in users:
            if user.roles.value == userRole:
                responsibilityUserNames.append(user.userName)
        return responsibilityUserNames

    
    def getAllSpecialItemNames(self, tableName = ItemHeader.DEPARTMENT.value or ItemHeader.SUBJECT.value or 
        ItemHeader.OBJECT.value or ItemHeader.LOCATION.value or ItemHeader.GROUP.value): 
        self.load()

        match tableName:
            case ItemHeader.DEPARTMENT.value:
                table = self.departments
            case ItemHeader.SUBJECT.value:
                table = self.subjects
            case ItemHeader.OBJECT.value:
                table = self.objects
            case ItemHeader.LOCATION.value:
                table = self.locations
            case ItemHeader.GROUP.value:
                table = self.groups
    
        itemNames = []
        for item in table:
            itemNames.append(item.getName())
        return itemNames