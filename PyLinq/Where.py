from py_linq import Enumerable

marks = Enumerable([25, 49, 50, 80, 90])
passing = marks.where(
    lambda x: (x > 50 or x < 40) and x > 85
)  # results in [50, 80, 90]
print(passing)


values = Enumerable(
    [
        {"name": "Mrinal", "age": 41},
        {"name": "Smith", "age": 41},
        {"name": "Molu", "age": 9},
        {"name": "Goosy", "age": 4},
    ]
)

result = values.where(lambda x: x["age"] > 40)

print(result)
