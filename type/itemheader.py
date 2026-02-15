from enum import Enum

class ItemHeader(Enum):
    OBJECT = "Gegenstand"
    GROUP = "Gruppe"
    DEPARTMENT = "Abteilung"
    SUBJECT = "Fach"
    LOCATION = "Ort"
    RESPONSIBLE = "Verantwortlicher"
    STATE = "Zustand"