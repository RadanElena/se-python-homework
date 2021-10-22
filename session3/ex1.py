"""
    Ex. 1: Functia de mai jos returneaza X la puterea Y.
    Modificati aceasta functie incat sa intoarca X la puterea Y la puterea Z.
"""


def power(x, y, z = 1):             # variable z is optional, so the power function can be used without declaring z (in that case z = 1)          
    return x **(y ** z) 

a = int(input("a: "))
b = int(input("b: "))

user = input("\nDo you wanna calculate a ^ b? if yes, press 1 , \nIf you wanna calculate a ^ (b ^ c) then, press 2: ")

if user == "1":
    z = power(a,b)
    print(f"\n{a} ^ {b} = {z}")
elif user == "2":
    c = int(input("\nc: "))
    z = power(a,b,c)
    print(f"\n{a} ^ ({b} ^ {c}) = {z}")
