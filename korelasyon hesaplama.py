#!/usr/bin/env python
import math
x = [1, 2, 5, 7, 8, 12, 15, 17, 18]
y = [4, 8, 9, 13, 16, 19, 21, 25, 27]


# r() = korelasyon, E() = toplam, n = grupların eleman sayısı, sqrt() = karekök
# r(x, y) = (E(x*y)-(E(x)*E(y)/n)) /  sqrt((E(x^2)-E(x)^2/n)*(E(y^2)-E(y)^2/n))

# Listedeki elemanları toplama fonksiyonu
def E(liste):
    toplam = 0
    for i in range(len(liste)):
        toplam += liste[i]
    return toplam

# Listenin karesini alma fonksiyonu
def kare(liste):
    a = liste.copy()
    for i in range(len(liste)):
        a[i] = liste[i] * liste[i]
    return a

# İki listeyi çarpma fonksiyonu
def carpim(listebir, listeiki):
    finalliste = []
    for i in range(len(listebir)):
        finalliste.append(listebir[i] * listeiki[i])
    return finalliste   

# Korelasyon fonksiyonu
#def r(listebir, listeiki):
#    return (E(carpim(listebir, listeiki)) - (E(listebir)*E(listeiki)/len(listeiki)) / math.sqrt((E(kare(listebir))-E(listebir)*E(listebir)/len(listebir))*(E(kare(listeiki))-E(listeiki)*E(listeiki)/len(listeiki))))
def r(listebir, listeiki):
    n = len(listebir)
    nom = (n*E(carpim(listebir, listeiki)) - E(listebir)*E(listeiki))
    denom = math.sqrt((n*E(kare(listebir)) - E(listebir)*E(listebir)) * (n*E(kare(listeiki)) - E(listeiki) * E(listeiki)))
    return nom/denom
# MegaCrafter thank you for your contribution

# Çalıştır

print(r(x, y))
print(x)