'''
access points ==> 1.public 2.protected 3.private 
سطوح دسترسی کلاس ها
'''

class Person:
    name = 'Armin' #public
    _age = 22  # protected (only for this class and children)
    __height = 185  # private (only for this class)

    def __Showp(self): # private (only for this class)
        print('show method is private')
    
class Male(Person):
    def Show(self):
        print(self.age)


print(Person.name) #public
# print(Person.__height) #private  and you get an  error  
print(Person._Person__height) #private  and you dont get  an error becuase of Name mangling


        