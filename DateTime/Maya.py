import maya

dt = maya.parse('2018-04-29').datetime()
print(dt.date(),type(dt.date()))
print(dt.time(),type(dt.time()))
print(dt.tzinfo)