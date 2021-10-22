"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
import string

def func(s):
    alphabet_string = string. ascii_lowercase
    l = []
    for i in s:
        l.append(alphabet_string[alphabet_string.index(i)+1])
    
    str = "".join(l)
    return str

"""
    If string contains "z" then the program will get an error because "z" is the last char in the alphabet,
    there is no more char in the alphabet to be replaced with
"""
user = input("Introduce a string: ")
print(func(user))