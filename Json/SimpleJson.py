import json

value = {"Key1": "Value'1"}
print(value)
jsonValue = json.dumps(value)
print(jsonValue)
print(type(jsonValue))
dataValue = json.loads(jsonValue)
print(dataValue)
print(type(dataValue))


