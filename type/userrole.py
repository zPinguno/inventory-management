from enum import Enum

class UserRole(Enum):
    RESPONSIBLE = "Verantwortlicher"
    ADMIN = "Admin"
    TEACHER = "Lehrer"
    BORROWER = "Ausleiher"

def normalizeRoleText(text):
    match text:
        case 'Verantwortlicher':
            return UserRole.RESPONSIBLE
        case 'Admin':
            return UserRole.ADMIN
        case 'Lehrer':
            return UserRole.TEACHER
        case 'Ausleiher':
            return UserRole.BORROWER

        case _:
            if isinstance(text, UserRole):
                return text
            return None