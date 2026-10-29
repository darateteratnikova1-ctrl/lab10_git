class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
    def info(self):
        return f"{self.name}, {self.group}"
