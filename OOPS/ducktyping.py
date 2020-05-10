# if a bird swims and quacks like a duck then it is a duck

class Laptop:
    def code(self,ide):
        ide.execute()

class VSCode:
    def execute(self):
        print("I am executing my code")
class PyCharm:
    def execute(self):
        print("I work only in Python")

lap1=Laptop()
ide=VSCode()
pyide=PyCharm()
lap1.code(pyide)
lap1.code(ide)

