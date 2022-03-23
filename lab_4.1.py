import random
# Zadanie 1

liczba = 2 * (random.randint(0,30))

plik = open("tekst.txt", "w+")
plik.writelines(str(liczba))
plik.close()

#Zadanie 2

plik = open("tekst.txt", "r")
odczyt = plik.readlines()
print(odczyt)
plik.close()

#Zadanie 3

with open("tekst.txt", "w+") as plik:
    liczba = liczba / 2
    plik.writelines("Wpisana liczba, ktora zostala pomnozona przez 2 to: %(x)d\n" % {'x': liczba})

with open("tekst.txt", "r") as plik:
    for odczyt in plik:
        print(odczyt, end='')

#Zadanie 4

class NaZakupy:
    nazwa_prodkutu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jednostki = 0.0

    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa_prodkutu = nazwa
        self.ilosc = ilosc
        self.jednostka_miary = jednostka
        self.cena_jednostki = cena

    def wyswietl_produkt(self):
        print(self.nazwa_prodkutu + " " + str(self.cena_jednostki) + "zl\\" + self.jednostka_miary)

    def ile_produktu(self):
        return str(self.ilosc) + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jednostki


ziemniak = NaZakupy("Marchewka", 2, "kg", 2.79)
ziemniak.wyswietl_produkt()
print(ziemniak.ile_produktu())
print(ziemniak.ile_kosztuje())

#Zadanie 5

class CiagArytmetyczny(self):
    wartosci = []

    def wyswietl_wyrazy(self):
        print(self.wartosci)

    def pobierz_wyrazy(self):
        n = input("Ile wyrazow: ")
        for i in range(int(n)):
            a = int(input("Podaj wyraz a%(x)d: " % {'x': i + 1}))
            self.wartosci.append(a)

    def pobierz_parametry(self, a1, r, n):
        self.wartosci = [a1 + i * r for i in range(n)]

    def policz_sume(self):
        suma = 0
        for i in range(len(self.wartosci)):
            suma += self.wartosci[i]
        return suma

    def policz_elementy(self):



#Zadanie 6

class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, kroki = 1):
        self.y += self.krok * kroki

    def idz_w_dol(self, kroki = 1):
        self.y -= self.krok * kroki

    def idz_w_prawo(self, kroki = 1):
        self.x += self.krok * kroki

    def idz_w_lewo(self, kroki = 1):
        self.x -= self.krok * kroki

    def gdzie_jestes(self):
        return self.x, self.y


robak = Robaczek(1, 1, 1)
robak.idz_w_lewo(2)
robak.idz_w_dol()
print(robak.gdzie_jestes())
robak.idz_w_prawo(3)
robak.idz_w_gore()
print(robak.gdzie_jestes())