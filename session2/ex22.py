"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
# Am creat o variabila 'user' a carui valoare este atribuita de la tastatura
user = input("Introduceti un string: ")

# Am creat o variabila 'string'
string = ""

"""
    Cu ajutorul unui 'for' am alternat literele din variabila 'user'(le-am marit sau micsorat), 
    fara a schimba defapt variabila, si am introdus noile litere alterate in variabila 'string'
"""

for i in range(len(user)):
    if (
        i % 2 == 0
    ):  # literele cu index par din user le-am marit si concatenat in variabila string
        string = string + user[i].upper()
    else:
        string = (
            string + user[i].lower()
        )  # literele cu index impar din user le-am micsorat si concatenat in variabila string

# Am afisat variabila string
print(string)
