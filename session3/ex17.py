"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""
import random


def append_text_file(func):
    def wrapper(x):
        message = func(x)
        f = open("output17.txt", "a")
        f.write(f"{message}\n")
        f.close()
        f = open("output17.txt", "r")
        print(f.read())
        f.close()

    return wrapper


@append_text_file
def f(x):
    random_string = ""
    while x:
        random_string += random.choice(["a", "b", "c", "d", "e", "f", "g", "h"])
        x -= 1
    return random_string


user = int(input("Number = "))
f(user)
