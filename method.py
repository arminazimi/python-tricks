'''

methods in python => 1.regular 2.class 3.static

'''
import datetime

class Car:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def Show(self):
        print(f'{self.name} has {self.age} years old')

    @classmethod
    def agecal(cls,name , age):
        return cls(name , datetime.datetime.now().year - age)
    
    @staticmethod
    def is_old(age):
        if age > 15:
            print('yes')
        else:
            print('no')


# regular
c2 = Car('pride', 5)
c2.Show()
   
#  @classmethod
c1 = Car.agecal('pride', 2010)
print(c1.age)

#@staticmethod
Car.is_old(18) 