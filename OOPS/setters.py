class Geek():
    def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
    def get_age(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
    def set_age(self, a): 
         print("setter method called") 
         self._age = a 
  
     # function to delete _age attribute 
    def del_age(self): 
         del self._age 
    
    #  decorator
    age = property(get_age, set_age, del_age)  
  
mark = Geek() 

mark.age = 18
  
print(mark.age)