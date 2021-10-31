"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""

import json


def read_from_file(file):
    with open(f"{file}.json", "r") as f:

        json_object = json.load(f)

    print(json_object)
    print(type(json_object))


name = "output19"

read_from_file(name)
