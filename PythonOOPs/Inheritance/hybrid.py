class Student:
    def __init__(self, name):
        self.name = name

class Sports:
    def __init__(self, sport):
        self.sport = sport

    def play(self):
        return f"Plays {self.sport}"

# Hybrid Inheritance (Combines multiple & multilevel inheritance)
class AcademicStudent(Student):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def study(self):
        return f"Studies {self.subject}"

class StudentAthlete(AcademicStudent, Sports):
    def __init__(self, name, subject, sport):
        AcademicStudent.__init__(self, name, subject)
        Sports.__init__(self, sport)

    def get_info(self):
        return f"{self.name} studies {self.subject} and also plays {self.sport}"

# Creating object
hybrid = StudentAthlete("Bala", "Mathematics", "Football")
print(hybrid.get_info())
