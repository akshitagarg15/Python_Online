# iterable-->__iter__()
#iterator--> __next__()
# iteration

n=[1,2,3,4,5,8,6]

# for i in n:
#     print(i)
it=iter(n)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

def gen(n):
    for i in range(n):
        yield i
g=gen(5)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
print(g)