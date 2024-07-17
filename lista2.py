
print("imie"*7)

print("imie\n"*5)

from random import randint
numbers = [5, 12, 7, 18, 20, 2, 15, 9, 11, 3]
numbers = [randint(1, 20) for _ in range(20)]
print(numbers)

wysw = list(filter(lambda x: x > 10, numbers))
print(wysw)

gr = []

for i in numbers:
    if i > 10:
        gr.append(i)
        
print(gr)

gr = [i for i in numbers if i > 10]
print(gr)

tab = [x for x in range(50,150)]

print([x for x in tab if x%7==0 and x%3==0])
#print([x for x in tab if x%3==0])

slow = {"Polska": "Warszawa", 
        "Czechy": "Praga", 
        "Niemcy": "Berlin", 
        "Anglia": "Londyn",
        "Francja": "Paryż",
        "Stany Zjednoczone Ameryki": "Waszyngton",
        "Włochy": "Rzym",
        "Słowacja": "Bratysława",
        "Węgry": "Budapeszt",
        "Rosja": "Moskwa"
        }

for i in slow:
    print(slow[i])




for i in slow:
    if slow[i][0] == "A":
        print(slow[i])




for i in slow:
    if "e" in slow[i] or "E" in slow[i]:
        print(slow[i])




print(min(numbers), max(numbers))




import numpy as np

tab4 = np.random.rand(20)
print(tab4)
print(tab4.mean(), tab4.max(), tab4.min())




tab = np.random.randint(5, 16, size=(10, 20))

print(tab, "\n")

for i in range(len(tab)):
    sr = 0
    for j in tab[i]:
        sr = sr + j

    print(f"Średnia dla {i} wiersza: {sr/20}")
    print(f"Max liczba dla {i} wiersza: {np.max(tab[i])}")
    print(f"Min liczba dla {i} wiersza: {np.min(tab[i])}\n")
    sr = 0

def wieksze_od_10(lista):
    return [i for i in lista if i > 10]

print(wieksze_od_10(numbers))

def liczba_sumaryczna(slow):
    litery_panstw = 0
    litery_stolic = 0
    
    for i in slow:
        for _ in i:
            litery_panstw = litery_panstw + 1
            
    for i in slow:
        for _ in slow[i]:
            litery_stolic = litery_stolic + 1
            
    return litery_panstw, litery_stolic

print(liczba_sumaryczna(slow))

