class Zad7:
    def __init__(self, data):
        self.data=data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index % 2 == 0:
            self.index = self.index +2
        else:
            self.index = self.index +1

        return self.data[self.index]

lista = [i for i in range (0,100,3)]
x = Zad7(lista)

print(iter(x))
print(next(x))
print(next(iter(x)))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


