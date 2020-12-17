import random
from memoization import cached
from CustomMemoization import memoize

'''
===========================================================================================
'''

totalRecords = 100

def generateName():
    namePrefixes = ["M","N","Z"]    
    nameIds = range(1,10)
    name = random.choice(namePrefixes) + str(random.choice(nameIds))
    return name

def generateId():       
    ids = range(1,20)
    return random.choice(ids)

def generateLevel():       
    levels = ["Architect","Developer","Sr Developer","Manager","Director","Ceo"]
    return random.choice(levels)

def generateTraits():
    traits = ["excellent","satvic","yoga","good"]
    return random.choices(traits,k=2)

'''
===========================================================================================
'''

'''
Generate the Cache Key
'''
def GetKey(**kwargs):
    return kwargs["val"]

# Inprocess Cache
# # @cached(custom_key_maker=GetKey) 

# # # Distributed Cache
# # @memoize 
@cached(custom_key_maker=GetKey) 
def generateData(**kwargs):
    
    print("Generate Data")
    
    finalData = []
    
    gdCounter = 1
    
    while gdCounter < 100000:
        d = dict()
        d["id"] = generateId()
        d["name"] = generateName()
        d["level"] = generateLevel()
        d["traits"] = generateTraits()
        finalData.append(d)
        gdCounter = gdCounter + 1
    
    return finalData
    
    
    
    