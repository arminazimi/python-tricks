'''
    Abstract Class
    Abstract Method
'''

from abc import ABC , abstractmethod

class A(ABC): #Abstract Class
    
    @abstractmethod #Abstract Method
    def show(self):
        pass


class B(A):
    def show(self):
        print('hi')


b = B()
b.show()
