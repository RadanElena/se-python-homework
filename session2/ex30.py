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
# Am creat variabila 'user' a carui valoare ii este atribuita de la tastatura
user = input("\nIntroduceti un string de tip paranteze: ") 

suma_paranteze1 = 0                 # suma paranteza de tip '()'
suma_paranteze2 = 0                 # suma paranteza de tip '[]'
suma_paranteze3 = 0                 # suma paranteza de tip '{}'

# Am creat cate o variabila de tip boolean ptr. fiecare tip de paranteza si initializat cu True
v_rotunda = True           
v_patrata = True
v_acolada = True

# Am verificat pe rand, cu ajutorul for-urilor si if-ului daca parantezele sunt inchise corect
# Pentru a fi mai usor de urmarit am creat un for de verificare pentru fiecare tip de paranteza in parte 
"""
    Logica dupa care a fost facut fiecare for a fost: 
    pentru ca o paranteza sa fie inchisa corect, la finalul verificarii suma_parantezei = 0 ( 0+1-1= 0 ) si
    cand verifica daca se deschide paranteza (ex. "(" sau "[" sau "{") suma_parantezei de acel tip, pana in acel moment, 
    sa fie mai mare sau egal cu 0 (daca ar fi < 0 ar insemna ca parantezele fie au inceput cu ")" sau "]" sau "}" 
    fie numarul lor este mai mare decat parantezele de deschidere deci parantezele sunt inchise gresit)
"""

for i in user:
    if i == "(" and suma_paranteze1 >= 0:
        suma_paranteze1 = suma_paranteze1 + 1
    elif i == "(" and suma_paranteze1 < 0:             
        v_rotunda = False                       
        break
    elif i == ")":
        suma_paranteze1 = suma_paranteze1 - 1 
    
if v_rotunda == True and suma_paranteze1 !=0 : 
    v_rotunda = False


for i in user:
    if i == "[" and suma_paranteze2 >= 0:
        suma_paranteze2 = suma_paranteze2 + 1
    elif i == "[" and suma_paranteze2 < 0:
        v_patrata = False
        break
    elif i == "]":
        suma_paranteze2 = suma_paranteze2 - 1 
    
if v_patrata == True and suma_paranteze2 !=0 :
    v_patrata = False


for i in user:
    if i == "{" and suma_paranteze3 >= 0:
        suma_paranteze3 = suma_paranteze3 + 1
    elif i == "{" and suma_paranteze3 < 0:
        v_acolada = False
        break
    elif i == "}":
        suma_paranteze3 = suma_paranteze3 - 1 
    
if v_acolada == True and suma_paranteze3 !=0 :
    v_acolada = False


# Am creat un if pentru a face verificarea finala si vedea daca tot stringul format din paranteze este inchis corect sau nu
if v_rotunda == True and v_patrata == True and v_acolada == True:
    print("Parantezele sunt inchise corect? {}".format(True))
else:
    print("Parantezele sunt inchise corect? {}".format(False))


