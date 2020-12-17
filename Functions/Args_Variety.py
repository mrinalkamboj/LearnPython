# Method Arguments Combining Example

# Simple / Standard positional argument
def standard_arg(arg):
    print(arg)


# Only Positional Argument
def pos_only_arg(arg, /):
    print(arg)


# Only Keyword Argument
def kwd_only_arg(*, arg):
    print(arg)


# Combined - All kinds of Argument
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
