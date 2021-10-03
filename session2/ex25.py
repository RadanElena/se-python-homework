"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa introduceti toate elemente intr-o lista si s-o afisati, dupa
    care va trebui sa creati un set (vezi ce e un set) din lista respectiva
    si sa il printati si pe acela.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa prima data: [1, 3, 4, 5, 5]
        Veti prina a doua oara: {1, 3, 4, 5}
"""

# Am afisat conditia pentru care loop-ul se opreste (l-am pus primul doar pentru ca mi se parea ca asa arata mai bine la ouput :D)
print("\nPentru a va opri, tastati 'exit'\n")

""" 
    Am creat o variabila 'user' a carui valoare ii este atribuita de la tastatura, si am lasat-o 
    initial de tip string pentru a se putea verifica usor conditia din 'while'
"""
user = input("Introduceti un numar: ")

# Am creat o lista goala, in care voi adauga ulterior valori cu ajutorul lui 'while'
l1 = []

"""
    Am creat un loop de tip 'while' a carui conditie sa se opreasca e sa se introduca 
    cuvantul 'exit' de la tastatura, cat timp acesta ruleaza, va adauga pe rand in lista 
    'l1' toate numerele introduse de la tastatura
"""

while user != "exit":
    l1.append(int(user))                           # am transformat variabila de tip string in int si am introduso in l1
    user = input("Introduceti un numar: ")

# Am afisat lista 'l1'
print("\nValorile listei sunt {}".format(l1))

# Am creat un set din lista l1
l2 = set(l1)

# Am afisat valorile setului l2
print("\nValorile setului sunt {}".format(l2))
