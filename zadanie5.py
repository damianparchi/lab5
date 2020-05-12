class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self,imie,nazwisko,pensja):
        Osoba.__init__(self,imie,nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "{} {} , jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


Damian = Pracownik("Damian","Parchi",3000)
Kamil = Menadzer("Kamil","Parchi",3400)

print(isinstance(Damian,Osoba))
print(isinstance(Damian,Pracownik))
print(isinstance(Kamil,Menadzer))
print(issubclass(Menadzer,Pracownik))