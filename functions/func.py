# defining

def hi():
    print("Hey how are you")

def checkEven(x):
    if x%2==0:
        print("even")
    else:
        print("odd")

# function with return keyword
def mul(n):
    num=3*n
    return num
# returning multiple values
def cal(a,b):
    add=a+b
    sub=a-b
    return add,sub

# calling
a=5
b=3
hi()
checkEven(12)
print(mul(a))
ans=mul(6)
print(ans)
addition,subtraction=cal(a,b)
print(addition)
print(subtraction)