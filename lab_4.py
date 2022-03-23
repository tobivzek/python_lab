class Ksztalty():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa ogolnych ksztaltow"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

class KwadratLiteraL(Kwadrat):
    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y

kwadrat = Kwadrat(5)

print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.dodaj_opis("Nasza figura to kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.3)
print(kwadrat.obwod())
print("")

litera_l = KwadratLiteraL(5)
print(litera_l.obwod())
print(litera_l.pole())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())
print("")

kwadrat = Kwadrat(10)
print(kwadrat)
print("")

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        #druga opcja - super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Manager(Pracownik):
    def przedstaw_sie(self):
        return "{} {}, jestem managerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

jozek = Pracownik('Josef', 'Bratan', 2000)
adrian = Manager('Adrian', 'Nowak', 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())
print("")

imie = "Janek"
it = iter(imie)
#print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("")

class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

napis = Wspak('Reks')
print(napis.__next__())
for a in napis:
    print(a)

print("")

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

gen = reverse("Feliks")
print(next(gen))
print("Marek")
print(next(gen))
print("")

litery = (litera for litera in "Zdzislaw")
#print(litery)
print(next(litery))