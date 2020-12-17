i = 5


def func(
    arg=i,
):  # copy by value, therefore arg gets the value 5 not 6, this is not copy by reference
    global i  # will make 1 assignment inside the fucntion as global variable, not local symbol table
    arg = i  # Assignd the Global value
    print(arg)


i = 6
func()
