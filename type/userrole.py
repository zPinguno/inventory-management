from enum import Enum

class UserRole(Enum):
    RESPONSIBLE = "Verantwortlicher"
    ADMIN = "Admin"
    TEACHER = "Lehrer"



def normalizeRoleText(text):
    match text:
        case 'Verantwortlicher':
            return UserRole.RESPONSIBLE
        case 'Admin':
            return UserRole.ADMIN
        case 'Lehrer':
            return UserRole.TEACHER

        case _:
            if isinstance(text, UserRole):
                return text
            return None