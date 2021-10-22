"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import random
import json

def rand_string(x):
    random_string = ""
    while x:
        random_string += random.choice(["a", "b", "c", "d", "e", "f", "g", "h"])
        x -= 1
    return random_string

def rand_number_list(n):
    l2 = [0,1,2,3,4,5,6,7,8,9,10]
    list_rand_num = []
    while n:
        num = random.choice(l2)
        list_rand_num.append(num)
        l2.remove(num)              
        n -= 1
    return list_rand_num

# The main function 
def json_file(name):
    values_list = []
    l = [3,4,5,6]
    a = 4
    while a != 0:
        num = random.choice(l)
        values_list.append(rand_string(num))
        a -= 1

    key_list = rand_number_list(4)
    key_list.sort()

    d = {}
    for i in range(len(key_list)):
        d[key_list[i]] = values_list[i]

    json_object = json.dumps(d, indent=4)

    with open(f"{name}.json", "w") as f:
        f.write(json_object)
  

user = "output19"

json_file(user)


