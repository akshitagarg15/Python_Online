from functools import reduce
l=[1,2,3,4,5,6]
# filter(function,iterable)
# filter


even=list(filter(lambda n: n%2==0,l))
print(even)

# map
sqr=list(map(lambda n: n*n,even))
print(sqr)

# reduce
sum=(reduce(lambda a,b: a+b,l))
print(sum)


