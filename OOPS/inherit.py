# single inheritance 

class Mammal:
    power=20

    def __init__(self,color):
        self.color=color

    def walk(self):
        print(" All mammmals can walk")

class Human(Mammal):
    power=50
    noOfLegs=2
    noOfeyes=2

    def __init__(self,intel,gen):
        super().__init__("blue")
        self.intel=intel
        self.gen=gen

    def talk(self):
        print("Humans can talk")
    def walk(self):
        print("Human can run fast")


m=Mammal("Black")
print(m.color)
karan=Human(75,'M')
print(karan.noOfeyes)
print(karan.noOfLegs)
karan.talk()
karan.walk()
print(karan.power)
print(karan.color)
