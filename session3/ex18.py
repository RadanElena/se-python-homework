"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def f(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + f(a_list[1:])


l2 = []
user = input("Number: ")
print("\nTo stop type exit\n")

while user != "exit":
    a = int(user)
    l2.append(a)
    user = input("Number: ")

print(f"\nThe sum of the elements from the list {l2} is {f(l2)}")
