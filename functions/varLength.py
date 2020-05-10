def my_fun(**kwargs):
    for key,Val in kwargs.items():
        print(f"{key} {val}")


def varFunc(*args):
    sum=1
    for arg in args:
       sum+=arg
    print(sum)

varFunc(1,2,3,4,5)
my_fun(fname="john",lname="doe")