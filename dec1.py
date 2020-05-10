def func():
    print("Hello World")

func2=func
del func
# func2()

# returning a function
def funcret(num):
    if num==1:
        return print
    if num==0:
        return sum

ans=funcret(0)
# print(ans)
# print(funcret(1))

# passing a function
def execute(func):
    func("Hey I am printing")
    # print("Hey I am printing")

# execute(print)

# decorators--nesting functions


def smart(func):
    def inside(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inside


# div=smart(div)
# # calling
# div(2,4)

@smart
def div(a,b):
    print(a/b)

