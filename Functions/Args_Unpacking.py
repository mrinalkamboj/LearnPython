# Un-packing Arguments Already part of the List
args = [3, 6]
print(args)  # [3, 6] - Prints actual list
print(list(range(*args)))  # [3,4,5]  - Use Range to consider List end points


def parrot(voltage, state="a stiff", action="voom"):
    print("if you put", voltage, "volts through it.", end=" ")
    print("E's", state, "!")
    print("-- This parrot wouldn't", action, end=" ")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)  # Unpacks the Dictionary and fills the parameters
