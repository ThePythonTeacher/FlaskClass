class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Student Name: {self.name}"

class Undergraduate(Student):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def get_course(self):
        return f"{self.name} is studying {self.course}"


class PhDStudent(Undergraduate):
    def __init__(self, name, course, research):
        super().__init__(name, course)
        self.research = research

    def get_research(self):
        return f"{self.name} is researching on {self.research}"


phd = PhDStudent("Bala", "Computer Science", "AI & ML")
print(phd.get_name())
print(phd.get_course())
print(phd.get_research())
