from just_trying import Person
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print('welcome', self.first_name, self.last_name, 'to the class of', self.graduationyear)
x = Student('mike', 'john', 2015)
x.welcome()