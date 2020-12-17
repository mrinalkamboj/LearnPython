words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w), sep=":")


users = [
    {"name": "Mrinal", "active": True},
    {"name": "Arjun", "active": False},
    {"name": "Smith", "active": True},
]

for user in users:
    if user["active"]:
        print("{} is Active".format(user["name"]))
    else:
        print("{} is InActive".format(user["name"]))

for cnt in list(
    range(3)
):  # Range Provides us the Iterator, which can be converted to List or directly iterated
    print(cnt)
