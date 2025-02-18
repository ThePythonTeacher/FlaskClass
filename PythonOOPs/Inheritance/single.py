class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Student Name: {self.name}, Age: {self.age}"


class ResearchScholar(Student):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree

    def get_details(self):
        return f"{super().get_details()}, Degree: {self.degree}"

scholar = ResearchScholar("Bala", 25, "PhD")
print(scholar.get_details())
