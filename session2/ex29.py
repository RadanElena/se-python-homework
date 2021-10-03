"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
# Am creat variabila 'user' a carui valori ii sunt atribuite de la tastatura
user = input("\nIntroduceti un string: ").lower()           # l-am formatat sa fie doar cu litere mici pentru a imi fie mai usor sa numar cu 'for'

# Am creat doua contoare, unul pentru numarul de vocale si unul pentru numarul de consoane
n_vocale = 0
n_consoane = 0

# Am creat un 'for' care imi numara practic numarul de vocale si consoane din stringul introdus de la tastatura
for i in range(len(user)):
    if user[i] == "a" or user[i] == "e" or user[i] == "i" or user[i] == "o" or user[i] == "u":
        n_vocale = n_vocale + 1
    else:
        n_consoane = n_consoane + 1

# Am afisat numarul de vocale si consoane din stringul introdus de la tastatura
print("\nStringul '{}' are: \n{} vocale; \n{} consoane;".format(user, n_vocale, n_consoane))

