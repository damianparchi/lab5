class Metody:
    def __init__(self,x):
        self.x=x
    
    def __gt__(self,zmienna):
        return self.x > zmienna.x
    
    def __ge__(self,zmienna):
        return self.x >= zmienna.x
    
    def __lt__(self,zmienna):
        return self.x < zmienna.x

    def __le__(self,zmienna):
        return self.x <= zmienna.x

class Kwadrat(Metody):
    def __gt__(self,zmienna2):
        return self.x > zmienna2.x
x1 = Metody(50)
x2 = Metody(60)

print(x1.__gt__(x2))
print(x1.__ge__(x2))
print(x1.__lt__(x2))
print(x1.__le__(x2))

x3 = Kwadrat(20)
x4 = Kwadrat(10)

print(x3.__gt__(x4))
