#zadanie_1
zmint1 = 5
zmint2 = 10
zmchar1 = "pierwszy string"
zmchar2 = "drugi string"
zmfl1 = 2.33
zmfl2 = 3.14
zmc1 = 3+2j
zmc2 = 10+1j

print(zmint1, zmint2, zmchar1, zmchar2, zmfl1, zmfl2, zmc1, zmc2, sep="\n")
#zadanie_2
print("Wprowadz dwie liczby aby przeprowadzic dzialanie")
a = float(input("Wprowadz pierwsza liczbe: "))
b = float(input("Wprowadz druga liczbe: "))
print("Wybierz dzialanie ktore ma byc wykonane\n1.Dodawanie\n2.Odejmowanie\n3.Mnozenie\n4.Dzielenie\n5.Dzielenie Calkowite\n6.Potegowanie")
c = int(input("Numer dzialania: "))
if c == 1:
    print(a + b)
if c == 2:
    print(a - b)
if c == 3:
    print(a * b)
if c == 4:
    print(a / b)
if c == 5:
    print(a // b)
if c == 6:
    print(a ** b)
#zadanie_3
a = 5
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 2
print(a)
#zadanie_4
import math
print(math.exp(10))
print((math.log(5+(math.sin(8)**2)))**(1/6))
print(math.floor(3.55))
print(math.ceil(4.80))
#zadanie_5
import sys
a = "T"
b = "O"
c = "B"
d = "I"
e = "A"
f = "S"
g = "Z"
f = a+b+c+d+e+f+g
print(f.capitalize())
#zadanie_6
a = 'la la la la la la'
print(a.count('la'))
#zadanie_7
przedmiot = 'Wizualizacja'
print(przedmiot[1], przedmiot[-1])
#zadanie_8
a = "la la la la"
print(a.split())
#zadanie_9
a = "Rozne zmienne"
b = 10.15
c = 2
