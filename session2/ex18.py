"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
user = input("Stringul dumneavoastra este: ")
x = int(input("Introduceti un numar: "))
y = int(input("Introduceti un numar: "))

print(user[x:y+1:1])