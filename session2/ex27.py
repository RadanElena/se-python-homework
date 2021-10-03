"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""

# Am important functiile de care aveam nevoie
import random
import string

# Am creat variabila 'user' a carui valori ii sunt atribuite de la tastatura
user = int(input("\nIntroduceti un numar: "))

# Am creat o variabila 'list_strings' in care am importat tot alfabetul (doar cu litere mici)
list_strings = string.ascii_lowercase             # initial variabila nu este lista si e de forma 'abcdef......z'

# Am separat caracterele unele de celelate si am transformat variabila 'list_strings' in lista 
list_strings = list(map(chr, range(ord('a'), ord('z')+1)))       #functia map itereaza, separand practic characterele unele de celelalte

# Am creat un string 'aleatoriu'
aleatoriu = ""

"""
    Am creat un 'for' pentru a introduce charactere random din lista in stringul creat 
    (numarul de charactere introduse = numarul introdus de la tastatura)
"""

for i in range(user):
    aleatoriu = aleatoriu + random.choice(list_strings)          # functia random.choice va selecta aleatoriu charactere din list_strings

# Am afisat stringul aleatoriu creat
print("Stringul aleatoriu creat este: {}".format(aleatoriu))