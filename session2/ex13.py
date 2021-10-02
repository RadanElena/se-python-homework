"""
    Veti primi 2 numere intregi de la tastatura (x si y).
    Va trebui sa le convertiti si apoi sa printati valorea lui x la puterea y.

    exemplu:
        Veti primi: 2 si 3
        Veti printa: 8
"""

x = int(input("Valoarea lui x este: "))
y = int(input("Valoarea lui y este: "))

print("Valoarea lui x la puterea y este: {}".format(pow(x,y)))

