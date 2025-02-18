class Sports:
    def __init__(self, sport):
        self.sport = sport

    def play(self):
        return f"Plays {self.sport}"

class Academics:
    def __init__(self, subject):
        self.subject = subject

    def study(self):
        return f"Studies {self.subject}"


class StudentAthlete(Sports, Academics):
    def __init__(self, name, age, sport, subject):
        Sports.__init__(self, sport)
        Academics.__init__(self, subject)
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, Age: {self.age}, {self.play()}, {self.study()}"

# Creating object
athlete = StudentAthlete("Bala", 25, "Cricket", "Mathematics")
print(athlete.get_info())
