"""
    Ex. 2: Modificati urmatoarea bucata de cod astfel incat
    la rulare, rezultatul afisarii sa fie cele 2 liste concatenate.
    HINT: Exista mai multe moduri prin care puteti face asta.
"""
# Ii dam variabilei l1 ca si valoare o lista cu 4 elemente (1,2,3,4)
# si variabilei l2 ca valoare o lista cu 4 elemente (5,6,7)
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

# Metoda 1
l3 = l1 + l2

# Afisam listele l1 si l2 separat.
# Pentru a vedea rezultatul, rulati acest script.
print(l1)
print(l2)
print(l3)        # print pentru afisarea celor 2 liste concatenate 

# Metoda 2

l4 = l1
for i in l2:
    l4.append(i)
print(l4)

