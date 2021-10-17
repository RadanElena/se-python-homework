"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
# Am creat o functie care verifica daca parantezele sunt inchise corect

def verficare_paranteze(myStr):
    paranteze_deschise = ["[", "{", "("]
    paranteze_inchise = ["]", "}", ")"]
    lista = []
    for i in myStr:
        if i in paranteze_deschise:
            lista.append(i)
        elif i in paranteze_inchise:
            pozitie = paranteze_inchise.index(i)
            if (len(lista) > 0) and (paranteze_deschise[pozitie] == lista[len(lista) - 1]):
                lista.pop()
            else:
                return "Parantezele sunt inchise gresit."
    if len(lista) == 0:
        return "Parantezele sunt inchise corect."

# Am creat variabila 'user' a carui valoare ii este atribuita de la tastatura
user = input("\nIntroduceti un string de tip paranteze: ") 
print(verficare_paranteze(user))