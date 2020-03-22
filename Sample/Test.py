import sys

# print(sys.version, sys.executable, sep="\n", end="\n")
print(sys.executable, sep="\n", end="\n")


def Greet(whom1, whom2, whom3):
    greeting = "Hello, {} {} {}".format(whom1, whom2, whom3)
    return greeting


print(
    Greet("Mrinal", "Molu", "Smith"), Greet("DJ", "Goosy", "Shamin"), sep="\n", end="\n"
)

name = input("Your name please ::")

print("Hi,", name)
