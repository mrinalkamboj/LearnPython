# Lambda Returns the Anonymous Functions

# Returns the anonymous function which adds 2 nos
# One number is initially supplied second one is added via lambda
def make_incrementor(n):
    return lambda x: x + n


AnonyFunc = make_incrementor(21)  # Value n is supplied
print(AnonyFunc(21))  # Value x is supplied
print(AnonyFunc(42))  # Value x is supplied

# Returns the anonymous function which adds 2 nos
# Both numbers are supplied intially, Lambda function is empty
def make_incrementor_1(x, n):
    return lambda: x + n


AnonyFunc = make_incrementor_1(21, 21)
print(AnonyFunc())


def KeyFunc(pairValue):
    return pairValue[1]


pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
# pairs.sort(reverse=True, key=lambda pair: pair[1]) # Can supply key via Lambda
pairs.sort(reverse=False, key=KeyFunc)  # Can supply key via separate Function
print(pairs)
