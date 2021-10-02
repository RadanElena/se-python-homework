"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
x = input("Introduceti un cuvant: ")

l1 = []

for i in x:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        l1.append(i)
    
print("Cuvantul introdus are {} vocale".format(len(l1)))
