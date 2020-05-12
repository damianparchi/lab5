class Kwadrat():

    def __init__(self, x):
        self.x = x
        self.y = x
    
    def __add__(self,zmienna):
        return self.x + zmienna.x


kwadrat1 = Kwadrat(5)
kwadrat2 = Kwadrat(6)

wynik = kwadrat1.__add__(kwadrat2)

print(wynik)