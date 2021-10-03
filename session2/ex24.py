"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""

# Am creat o variabila 'user' a carui valoare ii este atribuita de la tastatura
user = input("Introduceti un numar intreg: ")        # am lasat valoarea sa fie de tip string pentru a fi mai usor de inversat

# Am creat o variabila n1 a carui valoare este valoarea in oglinda a variabilei user (ex: user = '1232' atunci n1 = '2321')
n1 = user[::-1]

# Am transformat variabilele, din unele de tip string in unele de tip integer

user = int(user)
n1 = int(n1)

"""
    Am creat un if care verifica daca cele doua variabile sunt egale sau nu, 
    daca cele doua variabile sunt egale, inseamna ca variabila user este un numar palindrom 
"""
if user == n1:
    print(True)
else:
    print(False)