"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""
# Am creat o variabila 'user' a carui valoare ii este atribuita de la tastatura
user = input("Introduceti un string: ")

# Am creat un "if" ce verifica daca stringul introdus este palindrom
if user == user[::-1]:        # user[::-1] intoarce in oglinda cuvantul (de exemplu "gol" devine "log")
    print(True)
else:
    print(False)
