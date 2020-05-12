class Point:
    counter = []

    def __init__(self,x,y):
        """Konstruktor punktu."""  
        self.x = x
        self.y = y
    
    def update(self,n):
        self.counter.append(n)
    
    def __gt__(self,zmienna):
        return self.counter > zmienna.counter

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(3,3)

print(p1.counter)
print(p2.counter)
print(p3.counter)
p1.update(5)
p2.update(3)
p3.update(1)
print(p1.__gt__(p3))
print(p1.counter)
print(p2.counter)
print(p3.counter)