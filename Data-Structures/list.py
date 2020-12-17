
squares = [1, 4, 9, 16, 25]  # List
print(squares)  # [1, 4, 9, 16, 25]
print(squares[0]) # 1
print(squares[-1]) # 25
squares += [36, 49, 64, 81, 100] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] (Append List like Concatenation)
print(squares)

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # Lists unlike Strings are Mutable
cubes.append(216)
print(cubes)
print(cubes.index(888)) # Exception as the element doesn't exist

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E'] # Replace the indexes 2,3,4 (2 - Inclusive, 5 - Exclusive)
print(letters)
letters[2:5] = [] # Remove the indexes 2,3,4 (2 - Inclusive, 5 - Exclusive)
print(letters)
letters[:] = [] # Clear whole list

a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n] # Creates a List of List DS
print(x) # [['a', 'b', 'c'], [1, 2, 3]]

# range is an iterator and is convverted to list
squares = list(range(10))
print(squares)

# list composition
squares = [x ** 2 for x in range(10)]
print(squares)

# similar list composition as above using Lambda
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

# list using another list with simple integers
result = list([2, 3, 4])
print(result)

# list using another list with complex object, which is dictionary in Json
result = list([{"name": "mrinal", "age": 41, "Job": "Chief Architect"}])
print(result)
