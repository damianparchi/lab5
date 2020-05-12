def generator(data):
    for index in range(0,len(data),1):
        yield data[index]


x = generator("Damian")

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

