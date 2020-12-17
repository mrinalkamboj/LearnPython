'''
Insert Query Preparation.
Takes Input as List of Dictionary as Input and returns output as colun names and data for insertion
'''
def BuildInsertParameters(insertData:[dict],insertDictionary:dict=None):

    # Columns for the Insertion Query
    insertionColumns = None
    DbInsertionColumns = []

    # Fetch all Insertion Columns
    if insertData is not None and len(insertData):
        insertionColumns = dict(insertData[0]).keys()

    for key in insertionColumns:

        colKey = key

        # insert Column Key
        if insertDictionary is not None and len(insertDictionary):
            if key in insertDictionary:
                colKey = insertDictionary.get(key)

        # Insert Key in the Db Insertion Columns      
        DbInsertionColumns.append(colKey)
    
    # All Insertion Data
    allInsertDataList = []

    # Traverse and Create the Insertion Query Data
    for valueDict in insertData:

        insertDataList = []

        for key in insertionColumns:            

            localValue = valueDict.get(key)
            
            if isinstance(localValue,str):
                insertDataList.append("'{localValue}'".format(localValue=localValue))
            elif isinstance(localValue,list):
                insertDataList.append("{" + ",".join(["'" + str(val) + "'" if isinstance(val,str) else str(val) for val in localValue]) + "}")
            else:
                insertDataList.append("{localValue}".format(localValue=localValue))

        allInsertDataList.append("("+",".join(insertDataList)+")")        
    
    resultColumns = ",".join(DbInsertionColumns)

    insertionResult = ",".join(allInsertDataList)    

    return (resultColumns,insertionResult)
        
        

'''
Build Insert Queries using the TableName and Insertion Data.
'''
def BuildInsertQuery(tableName,insertData,insertDictionary=None):
    
    # Fetch Insert Query Column Names and Insertion Data
    colNames,insertionData = BuildInsertParameters(insertData,insertDictionary)

    # Prepare Query
    query = "insert into {tableName} {colNames} values {insertionData}".format(tableName=tableName,
                                                                               colNames="("+colNames+")",
                                                                               insertionData=insertionData)
    return query

result = BuildInsertQuery("ClusterTable",[{"StoreCode":2,"StoreName":"Mrinal","StoreData":[5,6]}
                                ,{"StoreCode":3,"StoreName":"Molu","StoreData":[9,10,22]}],{"StoreCode":"sc","StoreName":"sn"})

print(result)
