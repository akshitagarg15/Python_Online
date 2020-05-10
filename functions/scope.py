# global
# local--> global--> error


a=10

def func():
    # global variable
    global a
    a=12
    print("inside",a)

func()
print(a)