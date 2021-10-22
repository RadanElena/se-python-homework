"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""
def mod(func):   
    def wrapper():
        user = func()
        l = []
        for i in user:
            l.append(i)
        print(l)
    return wrapper()

# decoarate me
@mod
def f():
    return 'cmi'


