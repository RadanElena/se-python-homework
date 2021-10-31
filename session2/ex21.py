"""
    Veti primi stringuri de la tastatura, pana cand primiti stringul 'exit'.
    Va trebui sa printati o lista cu stringurile primite fara ultimul caracter
    al fiecarui string.

    Observatii:
        - lungimea stringurilor va fi intotdeauan cel putin 1

    exemplu:
        Veti primi: 'cmi', 'center', 'for', 'machines'
        Veti printa: ['cm', 'cente', 'fo', 'machine']
"""
# Am creat variabila 'user' a carui valoare este data de la tastatura
user = input("Introduceti un cuvant: ")

"""
    Am creat o lista goala in care voi adauga ulterior toate valorile 
    introduse de la tastatura ce sunt diferite de 'exit'
"""
l1 = []

"""
    Pentru a introduce valorile in lista l1, am folosit un while care va itera 
    si introduce valorile in lista pana cand se va introduce cuvantul 
    'exit' de la tastatura
"""
while user != "exit":
    l1.append(user)
    print("Pentru a va opri tastati 'exit' ")
    user = input("Introduceti un cuvant: ")

# Am creat o noua lista in care voi introduce valorile formatate din l1 cu ajutorul lui 'for'
l2 = []

# Am creat un 'for' ce introduce stringurile din l1 in l2, dar inainte de a face asta le sterge ultima litera
for i in l1:
    l2.append(i[: len(i) - 1])

# Am afisat lista l2
print(l2)
