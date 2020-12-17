def ZipCustom(list1:list,list2:list,operator:str):
    return [str(list1[counter]) + operator + str(list2[counter]) for counter in range(len(list1))]

def BuildUpdateParameters(updateData:dict,updateDictionary:dict=None):

    # Columns for the Update Query
    updateColumns = None

    # Fetch all Update Columns
    if updateData is not None and len(updateData):        
        updateColumns = updateData.keys()

    updateColumnsList = [] # Column list for Update
    updateDataList = [] # Data list for Update

    # Traverse / Fetch Keys and Process
    for key in updateColumns:

        # Fetch Value per Key
        localValue = updateData.get(key)

        # Assign DB Column Key
        colKey = key

        # Update Column Key
        if updateDictionary is not None and len(updateDictionary):
            if key in updateDictionary:
                colKey = updateDictionary.get(key)

        # Append Column List
        updateColumnsList.append(colKey)
        
        # Process Data
        if isinstance(localValue,str):
            updateDataList.append("'{localValue}'".format(localValue=localValue))
        elif isinstance(localValue,list):
            updateDataList.append("{" + ",".join(["'" + str(val) + "'" if isinstance(val,str) else str(val) for val in localValue]) + "}")
        else:
            updateDataList.append("{localValue}".format(localValue=localValue))        
    
     # Zip and Join Data
    updateParameterResult = ",".join(ZipCustom(updateColumnsList,updateDataList,"="))

    return (updateParameterResult)

result = BuildUpdateParameters({"StoreCode":2,"StoreName":"Mrinal","StoreData":[5,6]},{"StoreCode":"sc","StoreName":"sn"})

print(result)