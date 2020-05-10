# Multiple
# __init__ -->constructor
class A():
    def __init__(self):
        print("I am in init A")
    def guard(self):
        print("A is the guardian")
    # print("I am in class A")

class B():
    def __init__(self):
        print("I am in init B")
    def guard(self):
        print("B is the guardian")
    # print("I am class B")

class C(A,B):
    def __init__(self):
        super().__init__()
        
    # print(" I am in class C")

joe=C()
# joe.guard()
