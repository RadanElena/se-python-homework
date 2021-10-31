"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""

user = input("Introduceti un string: ")

"""
    Deoarece nu putem adauga direct valori intr-un tuple (odata creat, nu ii poti adauga ulterior valori),
     mai intai am creat o lista pentru a introduce literele stringului
"""
list = []

for i in user:
    list.append(i)

# Am convertit lista int-un tuple

list_converted_in_tuple = tuple(list)

# Am afisat tuple-ul
print(list_converted_in_tuple)
