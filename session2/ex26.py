"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""

# Am creat variabila 'user' a carui valori ii sunt atribuite de la tastatura
user = input("\nIntroduceti un numar: ")

# Am creat un loop ce se va opri numai atunci cand este introdus cuvatul 'exit' de la tastatura
while user != 'exit':
    if int(user)%2 == 0:
        print("\nNumarul introdus este par? {}".format(True))
    elif int(user)%2 != 0:
        print("\nNumarul introdus este par? {}".format(False))
    user = input("\nIntroduceti un numar sau tastati 'exit' pentru a va opri: ")
