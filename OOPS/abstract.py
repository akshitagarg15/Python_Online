# Abstract class and methods 
from abc import ABCMeta,abstractmethod

class Quad(metaclass=ABCMeta):
    @abstractmethod
    def PrintArea(self):
        return 0

class Rect(Quad):
    l=12
    b=15
    def __init__(self,s):
        self.side=s
    
    def PrintArea(self):
        print("area is" ,self.l*self.b)

class Square(Quad):
    s=12
    def __init__(self,s):
        self.side=s
    
    def PrintArea(self):
        print("area is" ,self.s*self.s)


r=Rect(4)
r.PrintArea()
s=Square(4)
s.PrintArea()
