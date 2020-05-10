# Access Specifiers
# Private--> double underscore (__salary) --> No one can access it 
# Public --> name --> anyone can access it
#Protected--> single underscore (_age) --> only child class will access it 


class Employee:
    var=4
    _protectsal=15000
    __password="ajkdnja"

class Programmer(Employee):
    sal=122

joe=Programmer()
print(joe.var)
print(joe._protectsal)
print(joe.__password)