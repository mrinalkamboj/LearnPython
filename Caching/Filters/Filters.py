from re import search
import maya 

'''
'''
def ExecuteNumberFilters(colValue,
                        operator:str,
                        filterValue):

    returnVal = None
    
    localValue = filterValue
    
    if operator == "==":
        returnVal = colValue == localValue  
    elif operator == ">=":
        returnVal = colValue >= localValue
    elif operator == ">":
        returnVal = colValue > localValue 
    elif operator == "<=":
        returnVal = colValue <= localValue
    elif operator == "<":
        returnVal = colValue < localValue
    else:
        returnVal = colValue == localValue
    
    return returnVal

'''
'''
def ExecuteStringFilters(colValue,
                        operator:str,
                        filterValue:str,
                        valueType=None):

    returnVal = None
    
    localValue = str(filterValue)
    
    if valueType is None:
        
        if operator == "==":
            returnVal = colValue == localValue  
        elif operator.lower() == "contains":
            returnVal = True if search(localValue,str(colValue)) else False
                
    elif valueType.lower() == "date":
        
        if operator == "==":         
            returnVal = maya.parse(colValue).date == maya.parse(localValue).date
        elif operator == ">":
            returnVal = maya.parse(colValue).date > maya.parse(localValue).date
        elif operator == ">=":
            returnVal = maya.parse(colValue).date >= maya.parse(localValue).date
        elif operator == "<":
            returnVal = maya.parse(colValue).date < maya.parse(localValue).date
        elif operator == "<=":
            returnVal = maya.parse(colValue).date <= maya.parse(localValue).date
        elif operator == "between":
            returnVal = maya.parse(localValue[0]).date <= maya.parse(colValue).date <= maya.parse(localValue[1]).date    
    
    return returnVal

'''
'''
def ExecuteListFilters(colValue,
                     operator:str,
                     filterValue):

    returnVal = None
    
    localValue = filterValue
    
    if operator.lower() == "contains":
        if isinstance(localValue,str):
            returnVal = localValue in list(colValue)
        else: # Assumption that Local Value is a list
            # returnVal =  set(localValue).issubset(set(data[colName]))
            returnVal =  all(item in list(colValue) for item in localValue)
    
    return returnVal

'''
'''
def ExecuteJsonFilters(data:dict,
                       colName:str,                       
                       operator:str, 
                       value,
                       valueType,
                       jsonColName):

    jsonColValue = data[colName.lower()][jsonColName.lower()]
    
    if isinstance(value,int) or isinstance(value,float):
        return ExecuteNumberFilters(jsonColValue,operator,value)
    elif isinstance(value,str) and isinstance(jsonColValue,str):
        return ExecuteStringFilters(jsonColValue,operator,value,valueType)
    elif isinstance(value,str) and isinstance(jsonColValue,list):
        return ExecuteListFilters(jsonColValue,operator,value)
    elif isinstance(value,list) and isinstance(jsonColValue,list):
        return ExecuteListFilters(jsonColValue,operator,value)
    elif isinstance(value,list) and isinstance(jsonColValue,str):
        return ExecuteStringFilters(jsonColValue,operator,value,valueType)

'''
'''
def ExecuteFilters(data:dict,colName:str,operator:str,value,valueType=None,jsonColName=None):
    
    if jsonColName is not None:
        return ExecuteJsonFilters(data,colName,operator,value,valueType,jsonColName)
    elif isinstance(value,int) or isinstance(value,float):
        return ExecuteNumberFilters(data[colName.lower()],operator,value)
    elif isinstance(value,str) and isinstance(data[colName],str):
        return ExecuteStringFilters(data[colName.lower()],operator,value,valueType)
    elif isinstance(value,str) and isinstance(data[colName.lower()],list):
        return ExecuteListFilters(data[colName.lower()],operator,value)
    elif isinstance(value,list) and isinstance(data[colName],list):
        return ExecuteListFilters(data[colName.lower()],operator,value)
    elif isinstance(value,list) and isinstance(data[colName],str):
        return ExecuteStringFilters(data[colName.lower()],operator,value,valueType)

'''
'''
def FetchFilters():
    
    datafilters = [
                        {
                            "colname":"name",
                            "operator": "contains",
                            "value":"Z",
                            "type":None,
                            "jsoncolumn":None
                            
                        },
                        {
                            "colname":"traits",
                            "operator": "contains",
                            "value": ["yoga"],
                            "type":None,
                            "jsoncolumn":None
                        },
                        {
                            "colname":"id",
                            "operator": ">",
                            "value": 10,
                            "type":None,
                            "jsoncolumn":None
                        },
                        {
                            "colname":"level",
                            "operator": "==",
                            "value": "Ceo",
                            "type":None,
                            "jsoncolumn":None
                        }    
                  ]
    
    return datafilters


## Local Filter Test

# # localfilters =  {
# #                     "colname":"name",
# #                     "operator": "contains",
# #                     "value":["Mrinal"],
# #                     "type":None,
# #                     "jsoncolumn":"a"                            
# #                 } 
                
    


# # data = {"name":{"a":["Mrinal"]}}

# # final = ExecuteFilters(data,localfilters["colname"],
# #                        localfilters["operator"],
# #                        localfilters["value"],
# #                        localfilters["type"],
# #                        localfilters["jsoncolumn"])

# # print(final)