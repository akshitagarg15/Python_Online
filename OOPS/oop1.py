class Student:
    # class variable
    noOfLeave=10
    # constructor
    def __init__(self,Sname,Sage,Ssec):
        # instance variable
        self.name=Sname
        self.age=Sage
        self.sec=Ssec

    # Instance methods
    # fetching details
    def printDetails(self):
        print(f"Name :{self.name} Age: {self.age}")
    
    # to change the values
    def changeSec(self,Csec):
        self.sec=Csec
    
    @classmethod
    def changeLeave(cls,new_leave):
        cls.noOfLeave=new_leave
    
    @classmethod
    def getLeave(cls):
        return cls.noOfLeave

    @staticmethod
    def info():
        print("This is Student class")




# object
sham=Student("sham",12,'A')
karan=Student("karan",12,'B')

# sham.printDetails()
# karan.printDetails()
# sham.changeSec('C')
# print(sham.sec)

# sham.changeLeave(45)
print(sham.getLeave())
print(Student.noOfLeave)
sham.changeLeave(55)
print(sham.getLeave())
print(Student.getLeave())
print(karan.getLeave())
print("after")
print(sham.getLeave())
print(karan.getLeave())
print(Student.getLeave())


# Student.changeLeave(18)
# print(karan.noOfLeave)
# Student.getLeave()

# Student.info()
# sham.info()

# print(sham.name)
# print(sham.age)
# print(sham.sec)

# print(karan.name)

# print(karan.noOfLeave)
# print(Student.noOfLeave)



# Student.noOfLeave=20
# karan.noOfLeave=12
# print(Student.noOfLeave)
# print(karan.noOfLeave)
# print(sham.noOfLeave)
# print(sham.__dict__)

