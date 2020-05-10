def cal(name,age):
    print(f"hey {name} your age is {age}")


# default function
def myFunc(name,age=20):
      print(f"hey {name} your age is {age}")

# variable length arguments
# * is for a variable length tuple or list
def varFunc(*args):
    sum=1
    for arg in args:
       print(arg)
       print(type(arg))
       sum+=arg
    print(sum)

def my_fun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} {v}")

# keyword arguments
# cal(age=22,name="John")
# myFunc('akshita')
# variable length 

varFunc(1,2,3,4,5,6)
my_fun(fname="john",lname="doe")