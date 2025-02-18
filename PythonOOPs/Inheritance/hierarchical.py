class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Student Name: {self.name}"

class ScienceStudent(Student):
    def get_department(self):
        return f"{self.name} is in the Science Department"

class ArtsStudent(Student):
    def get_department(self):
        return f"{self.name} is in the Arts Department"


science = ScienceStudent("Bala")
arts = ArtsStudent("Sundar")

print(science.get_name())
print(science.get_department())

print(arts.get_name())
print(arts.get_department())
