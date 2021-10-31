"""
    Ex. 1: Functia de mai jos returneaza X la puterea Y.
    Modificati aceasta functie incat sa intoarca X la puterea Y la puterea Z.
"""


def power(x, y, z):  
    return x ** (y ** z)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(f"{a} ^ ({b} ^ {c}) = {power(a, b, c)}")