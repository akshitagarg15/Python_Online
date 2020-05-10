# Multilevel

class A:
    var=2
    age=75
    # dib=True
    
    def say(self):
        print('This is class A')

class B(A):
    var=10
    # dib=True
    # age=70
    def __init__(self,dib):
        self.dib=dib
    def sayHi(self):
        print('This is class B')
    
    def dibInChild(self,other):
        return self.dib | other.dib
        # M.dib | F.dib

class C(B):
    dib=False
    def sayHi(self):
        print('This is class C')
    
    

M=B(False)
F=B(True)
res=M.dibInChild(F)
print("Chances of child having dib: ",res)
