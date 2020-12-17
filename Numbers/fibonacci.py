# Fibonacci Program using Python
a, b = 0, 1  # Multi variable assignment in the same line
while a < 10:  # While Looping
    print(a, b, a + b, sep=" ")  # Print Values
    a, b = b, a + b  # Increment Values


##########
# Result:
##########
# 0 1 1
# 1 1 2
# 1 2 3
# 2 3 5
# 3 5 8
# 5 8 13
# 8 13 21
