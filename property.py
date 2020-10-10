'''
@property in python

'''

class Person:
    def __init__(self , first , last):
        self.first = first
        self.last = last

    def fullname(self):
        return f'{self.first} {self.last}'

    @property  
    def email(self):
        return f'{self.first}_{self.last}@email.com'


a = Person('armin' , 'azimi')

print(a.first)
print(a.last)
print(a.email) # it is a def but you dont need to use () 
print(a.fullname())

