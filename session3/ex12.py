"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def decorator(func):
    def wrapper(x):
        func(x)
        f = open("output12.txt", "w")
        f.write(x)
        f.close()

        f = open("output12.txt", "r")
        print(f.read())  # this is only to verify the content of the "output12.txt" file
        f.close()

    return wrapper


# decorate me
@decorator
def f(x):
    print(x)


user = input("Introduce your message here: ")

f(user)
