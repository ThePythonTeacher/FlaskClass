class Student():
    def __init__(self, name, age, gender, dob):
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob

    @classmethod
    def print_details(cls):
        '''
          this is the class methos

        :return:
        '''

        cls.address = "This is bala from Chennai"
        return cls.address

    def method(self):
        return f"this is the new method  {self.name}"

    @staticmethod
    def stat_fucntion():
        return "this is our standard function"


class ResearchScholar(Student):
    def __init__(self, name, age, gender, dob, degree):
        super().__init__(name, age, gender, dob)
        self.degree = degree

    def call_additional_into(self):
        return (super(ResearchScholar, self).method()) + f" and I am doing {self.degree} "


init = ResearchScholar("bala", '25', 'male', '15-Jan', 'BE')

print(init.call_additional_into())
