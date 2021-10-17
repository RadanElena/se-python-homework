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
    paranteze_deschise = ["[", "{", "("]               # am creat cate o lista cu toate parantezele deschise si inchise
    paranteze_inchise = ["]", "}", ")"]                # indexul fiecarui tip de paranteza din parantezele deschise ii corespunde celui din paranteze inchise
    lista = []                                         # am creat o lista goala de care ma voi folosi pentru a verifica parantezele
    for i in myStr:                                    # for va itera pe rand fiecare character din string,
        if i in paranteze_deschise:                    # daca i este una din parantezele dechise, acesta va fi adaugat in lista 
            lista.append(i)                             
        elif i in paranteze_inchise:                   # daca i este una din parantezele inchise,
            pozitie = paranteze_inchise.index(i)       # ii se va verifica pozitia parantezei in lista de paranteze inchise (indexul rezultat ii corespunde parantezei deschise de acelasi tip din lista de paranteze_deschise) 
            if (len(lista) > 0) and (paranteze_deschise[pozitie] == lista[len(lista) - 1]):       # daca lungimea variabilei lista >0 si paranteza deschisa gasita in variabila paranteze_deschise este aceeasi cu ultima paranteza deschisa din variabila lista
                lista.pop()                            # daca conditia din if este verificata, paranteza verificata se elimina din lista
            else:
                return "Parantezele sunt inchise gresit."    # daca conditia din if nu este verificata, inseamna ca parantezele sunt inchise gresit
    if len(lista) == 0:                                      # daca s-au eliminat toate parantezele din lista, inseamna ca toate parantezele au fost inchise corect                
        return "Parantezele sunt inchise corect."

# Am creat variabila 'user' a carui valoare ii este atribuita de la tastatura
user = input("\nIntroduceti un string de tip paranteze: ")

# Am apelat functia si afisat rezultatul final
print(verficare_paranteze(user))