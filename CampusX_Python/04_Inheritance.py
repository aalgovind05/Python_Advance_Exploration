# parent class
class User:

    def __init__(self):
        self.name = 'Govind'

    def login(self):
        print('login')

# child class

class Student(User):         # this (User) now have connected parent class with child class so we can use that here

    def __init__(self):      # we have to erase this contructor code to access parent clase because there should be only one constructor to
        self.rollno = 100    # so delet child constructor

    def inroll(self):
        print('you have inroll in new course')


u = User()
s = Student()


print(s.inroll())
print(s.login())




#super()#

class Phone:
    
    def __init__(self,price,brand,camera):
        print('inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('buying phone')


class Smartphone(Phone):
    
    def buy(self):
        print('buying a smartphone')
        super().buy()


s = Smartphone(20000,'apple',14)
s.buy()
