import random
x = int(input("Podaj liczbę elementów: "))
lista1 = []

for i in range (x):
    n = random.randint(1,10)
    lista1.append(n)
print(lista1)
x1 = int(input("Podaj liczbe elementow dla drugiej listy: "))
lista2 = []

for i in range (x1):
    n2 = random.randint(5,15)
    lista2.append(n2)
print(lista2)
x3 = int(input("Podaj liczbe której szukasz: "))

if x3 in lista1:
    print("Liczba występuje w lista1")

elif x3 in lista2:
    print("Liczba występuje w lista2")

else:
    print("Nie ma takiej liczby w obu zestawach")