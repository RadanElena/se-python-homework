"""
    Veti primi un string de la tastatura.
    Veti primi un numar intreg de la tastatura, x.
    Va trebui sa creati un dictionar care sa contina ca si chei, toate numerele
    pana la x, iar ca si valori caracterele de pe indexurile corespunzatoare.

    Observatii:
        - lungimea stringului va fi mereu egala cu numarul primit
        - indexarea in python incepe de la 0 (prima cheie va fi 0)

    exemplu:
        Veti primi: 'cmi', 3
        Veti printa: {
            0: 'c',
            1: 'm',
            2: 'i'
        }
"""

user = input("Introduceti un string: ")
x = int(input("Numarul introdus trebuie sa fie egal cu lungimea stringului: "))

"""
    Pentru a ma asigura ca numarul introdus de la tastatura este egal cu lungimea stringului
    am folosit un while
"""
while x != len(user):
    print("Numarul introdus de dumneavoastra are o valoare diferita de cea a lungimii stringului!")
    x = int(input("Introduceti un numar egal cu lungimea stringului: "))

l1 = []           # am creat o lista in care voi adauga cu ajutorul unui 'for' toate literele din string
l2 = []           # am creat o lista in care voi adauga cu ajutorul unui 'for' toate cifrele de la 0 la x

for i in user:
    l1.append(i)

for i in range(x):
    l2.append(i)

# Am creat dictionarul 

d1 = {}

# Cu ajutorul lui 'for' for introduce valori in dictionar

for i in range(x):
    d1[l2[i]]=l1[i]

# Am afisat dictionarul
print(d1)

