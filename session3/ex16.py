"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""

def upper(my_str):
    my_str = my_str.upper()
    return my_str

def lower(my_str):
    my_str = my_str.lower()
    return my_str

user = input("Introduce a string: ")

def call_changers(func):
    def wrapper(my_str):
        if len(my_str) % 2 == 0:
            return (upper(my_str))
        else:
            return (lower(my_str))
            
    return wrapper

@call_changers
def f(user):
    return user

print(f(user))