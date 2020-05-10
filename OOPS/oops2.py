# dunder methods
# a=2
# b=3
# print(a+b)
# # behind the scenes
# print(int.__add__(a,b))

# c='d'
# d='e'
# print(c+d)
# print(str.__add__(c,d))

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        total_m1=self.m1+other.m1
        total_m2=self.m2+other.m2
        # print(f"total marks in m1{total_m1}, total marks in m2={total_m2}")
        s3=Student(total_m1,total_m2)
        return s3
    
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if(r1>r2):
            return True
        else:
            return False
    
    def __truediv__(self,other):
        return self.m1/self.m2
    
    # __str__ has more priority than __repr__
    # def __str__(self):
    #     return str(2/11)
    
    def __repr__(self):
        return str(2/11)





    
s1=Student(10,15)
s2=Student(45,15)
s3=s1+s2 
# print(s3)
# print(s3.m1)
# print(s3.m2)
# print(s1/s2)
print(s3)

if s1>s2:
    print("S1 has more marks")
else:
    print("S2 has greater")







