'''

encapsulation : setter, getter, deleter

'''
class Person:
    def __init__(self):
        self.__age = 0

    @property  
    def age(self):   #getter
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


p = Person()
p.age = 22
print(p.age)
# del p.age