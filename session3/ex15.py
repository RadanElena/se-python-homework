"""
    Ex. 15: Avem functia f care printeaza 'cmi'.
    Faceti in asa fel incat atunci cand apelam g(), sa printeze tot 'cmi'.

    Observatii:
        - nu aveti voie sa scrieti o functie g voi (def g(): blabla)
        - nu aveti voie sa folositi decoratori
"""

def f():
    print("cmi")

# Now g is a function too! It does the same thing as f function 
g = f

g()
