class Department:
    name: str
    id: int

    def __init__(self,name, id = None):
        self.name = name
        if id != None:
            self.id = id

    def getName(self):
        return self.name