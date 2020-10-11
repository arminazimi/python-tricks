'''

polymorphism : چندین زیر کلاس با نام متد های یکسان کارهای متفاوت بکنن

'''
from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('meoo')

class Dog(Animal):
    def talk(self):
        print('hopp')

a = Cat('a')
b = Dog('b')

# one method does two job
a.talk()   
b.talk()