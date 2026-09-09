# parent class
class User:

    def __init__(self):
        self.name = 'Govind'

    def login(self):
        print('login')

# child class

class Student(User):         # this (User) now have connected parent class with child class so we can use that here

    def __init__(self):
        self.rollno = 100

    def inroll(self):
        print('you have inroll in new course')
