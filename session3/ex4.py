"""
    Ex. 4: Mai jos aveti 2 functii:
        - add_prefix --> adauga un prefix primit ca parametru unui string
        primit tot ca parametru
        - generate_random_str --> genereaza un string aleator de dimensiune X,
        X fiind un parametru

        Va trebui sa scrieti o functie care sa adauge un sufix (add_suffix),
        dar acel sufix nu trebuie sa contina nicio litera din prefix.

        Sufixul si prefixul le veti primi ca si input de la tastatura, la fel si
        X, care este lungimea stringului aleator.
        In cazul in care sufixul are vreo litera pe care o are si prefixul,
        veti cere un sufix nou, pana cand este dat unul corect, sau pana cand
        a fost incercat de 3 ori. A 4-a oara veti printa stringul fara sufix.

    Rezultatul ar trebui sa arate asa:
        - pentru prefix = 'bla', sufix = 'cmi', x = 3 si un string aleator 'lol'
            ---> 'blalolcmi'
        - pentru prefix = 'bla', sufix = (pe rand, 'ba', 'la', 'bla') x = 3
        si un string aleator 'lol'
            ---> 'blalol'

    Orice e neclar, ma intrebati pe discord la orice ora, fara probleme.
"""

import random
from collections import Counter


def add_prefix(pfx, rand_str):
    return pfx + rand_str


def add_suffix(f, sfx):
    return f + sfx


# Nu am spus ca stringul generat aleator trebuie sa contina toate literele
def generate_random_str(str_length):
    rand_str = ""
    while str_length:
        str_length -= 1
        rand_str += random.choice(["a", "x", "c", "m", "i"])
    print(f"The generated string is {rand_str}")
    return rand_str


prefix = input("Give me an prefix\n")
x = int(input("Give me a number to generate the random string\n"))
suffix = input("Give me an suffix\n")

a = 0
while a != 3:

    # i made prefix_l and sufix_l and give them the lowercare values of prefix and suffix so the bellow check to not be key sensitive
    prefix_l = prefix.lower()
    suffix_l = suffix.lower()

    # common variable makes a list with the common characters between prefix_l, and sufix_l
    common = list(set([c for c in prefix_l if c in suffix_l]))

    if len(common) == 0:
        print(add_suffix(add_prefix(prefix, generate_random_str(x)), suffix))
        break
    elif len(common) != 0 and a < 2:
        a += 1
        suffix = input("Give me another suffix\n")
    elif len(common) != 0 and a == 2:
        a += 1
        print(add_prefix(prefix, generate_random_str(x)))
