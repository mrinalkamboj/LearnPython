# The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
# For example, the following function accumulates the arguments passed to it on subsequent calls:

# Mutable object like List gets the old value post modification
def func1(a, L=[]):
    L.append(a)
    return L


# Explicitly reassigning the value to empty the List
def func2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(func1(1))
print(func1(2))
print(func1(3))
print("\n")
print(func2(1))
print(func2(2))
print(func2(3))
