 import random
#
# #zadanie 1
#
# a=[1-x for x in range(1,10)]
# print(a)
# b=[4**x for x in range(8)]
# print(b)
# c=[x for x in b if x%2==0]
# print(c)
#
# #zadanie 2
#
# a=[]
# for x in range(10):
#     a.append(random.randrange(100))
#
# print(a)
#
# a1=[x for x in a if x%2==0]
#
# print(a1)
#
# #zadanie 3
#
# a={'mleko':'ml', 'mąka':'kg', 'ogórek':'sztuki', 'pomidory':'sztuki'}
# b={key: value for key, value in a.items() if value=='sztuki'}
#
# print(b)
#
# #Zadanie 4
#
# def czyprostokatny(a,b,c):
#     if((a**2)+(b**2)==(c**2)):
#         return 'jest prostokatny'
#     else:
#         return 'nie jest prostokatny'
# a=3
# b=4
# c=5
#
# print(czyprostokatny(a,b,c))
#
# #Zadnie 5
#
# def poletrap(a=5,b=3,h=4):
#     return ((a+b)*h)/2
#
# print(poletrap())
#
# Zadanie 6
#
# def iloczynciagu(a=1,b=4,ile=10):
#     suma=0
#     i=0
#     while(i<ile):
#         suma=suma+a
#         a=a*4
#         i=i+1
#     return suma
#
# print(iloczynciagu())
#
# #zadanie7
#
# def il_el_ciagu7 (* liczby) :
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in liczby:
#             iloczyn *= x
#         return iloczyn
#
# print(il_el_ciagu7(1,2,3,4))