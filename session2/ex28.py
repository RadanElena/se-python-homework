"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
# Am creat variabila 'user' a carui valori ii sunt atribuite de la tastatura
user = int(input("\nIntroduceti un numar: "))

# Am creat o variabila de tip int, caruia i-am atribuit initial valoarea zero
suma = 0

"""
    Am creat un 'for' care va face practic suma numerelor pana la numarul introdus 
    de la tastatura, iar valoarea o va atribui variabilei 'suma'
"""
for i in range(0, user + 1):
    suma = suma + i

# Am afisat suma numerelor
print("Suma numerelor de la 0 la {} este: {}".format(user, suma))
