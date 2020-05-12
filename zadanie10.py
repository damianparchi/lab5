import itertools

def x():
    lista = [1,2,3,4,5,6,7,8,9,10]
    for i in itertools.combinations(lista,3):
        yield print(i)

x=x()
while(x != 0):
    next(x)
