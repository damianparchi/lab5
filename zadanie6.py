class Wspak:
    def __init__(self, data):
        self.data=data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):

        self.index = self.index - 1
        return self.data[self.index]

x = Wspak("Ala ma kota")

print(x.__iter__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

y = Wspak([i for i in range(0,10,2)])

print(y.__iter__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
