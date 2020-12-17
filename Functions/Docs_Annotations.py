def my_function():
    """ 
          My Function Documentation.

          Intends to do basic work
    """
    pass


# Prints function documentation via internal method
print(my_function.__doc__)

# Prints Optional Functional Annotations (Which is Function's metadata including arguments and return type)
def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs


f(
    "spam"
)  # Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
