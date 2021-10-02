"""
    Ex. 8: Modificati urmatoarea bucata de cod astfel incat
    la rulare, daca valoarea care vine de la tastatura nu este 'cmi'
    sa afisam 'NOT OK'
"""

# In x vom salvea valoarea care vine de la tastatura
x = input()

# Daca valorea care vine de la tastatura este 'cmi', vom afisa 'OK'
if x == 'cmi':      # modificarea 1, am inlocuit "da" cu "cmi" pentru a afisa corect "OK"
    print('OK')
else:
    print('NOT OK')   # modificarea2, daca valoarea ce vine de la tastatura este alta decat 'cmi', va afisa 'NOT OK'
