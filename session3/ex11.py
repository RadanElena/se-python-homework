"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""
def logIn(func):
    user = func()
    def wrapper():
        f = open("output11.data", "a")
        f.write(f"Now the user {user} is logged in!")
        f.close()
        f = ("output11.data", "r")
        print(f.read())
        f.close()
    return wrapper

        

# decorate me
@logIn
def f():
    return "CMI"
