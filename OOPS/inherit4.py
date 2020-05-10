class A:
    def __init__(self):
        print("In init A")
    
    def feature1(self):
        print("In featue of class A")

class B(A):
    def __init__(self):
        
        print("In init B")
        super().__init__()
    
    def feature2(self):
        print("In featue of class A")

child=B()