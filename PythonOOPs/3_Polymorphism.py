class Home():
    def role(self):
        return " as father "


class Office(Home):
    def role(self):
        return  "as a TL"

class TutionCenter(Office):
    def role(self):
        return "as a teacher "

class Bala(TutionCenter):
    def role(self):
        return f"{TutionCenter.role(self)}, {Office.role(self)}, {super().role()}"



balas_role = Bala()

print(balas_role.role())




