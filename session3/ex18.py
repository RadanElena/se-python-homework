"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""

def f(aList):
   if len(aList) == 1:
        return aList[0]
   else:
        return aList[0] + f(aList[1:])


l2 = []
user = input("Number: ")
print("\nTo stop type exit\n")

while user != "exit":               
    a = int(user)
    l2.append(a)
    user = input("Number: ")

print(f"\nThe sum of the elements from the list {l2} is {f(l2)}")