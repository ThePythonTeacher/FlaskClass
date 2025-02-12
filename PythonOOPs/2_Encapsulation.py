class Student():
    def __init__(self, name, age, gender, dob, id):
        self.name = name
        self.age = age
        self.gender = gender
        self._dob = dob
        self.__id = id

    @classmethod
    def print_details(cls):
        '''
          this is the class methos

        :return:
        '''

        cls.address = "This is bala from Chennai"
        return cls.address

    def get_id(self):

        return f"The id {self.__id}"

    @staticmethod
    def stat_fucntion():
        return "this is our standard function"


class ResearchScholar(Student):
    def __init__(self, name, age, gender, dob, degree,id):
        super().__init__(name, age, gender, dob, id)
        self.degree = degree

    def call_additional_into(self):
        return (super(ResearchScholar, self).method()) + f" and I am doing {self.degree} "

    def get_id(self):
        return f"{super().get_id()}", "from Child "

#
# init = ResearchScholar("bala", '25', 'male', '15-Jan', 'BE')
#
# print(init.call_additional_into())


stud_obj = ResearchScholar("bala", "25", "male", "jan-15", 'BE', '20')

print(stud_obj.get_id())