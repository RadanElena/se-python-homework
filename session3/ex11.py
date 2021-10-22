"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""

def logIn(func):   
    def wrapper():
        user = func()
        f = open("output11.txt", "w")
        f.write(f"Now the user {user} is logged in!")
        f.close()
        f = open("output11.txt", "r")                 # i opened the file in the read mode for verification
        print(f.read())           
        f.close()
    return wrapper

# decorate me
@logIn
def f():
    return "CMI"

f()


