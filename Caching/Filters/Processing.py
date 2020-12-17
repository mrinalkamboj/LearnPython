from Filters import ExecuteFilters

import multiprocessing
import time

datafilters = []

def DataFilterProcessing(dataPoint):    
    if all([ExecuteFilters(dataPoint,f["colname"],f["operator"],f["value"]) for f in datafilters]):
        return dataPoint
    else:
        return


def ProcessData(dataTotal,filters,multiProcess:bool=True):
    
    startFilter = time.time()   
    
    global datafilters
    datafilters = filters
    filtered_result = None
    if multiProcess:
        print("Multi-Process")
        pool = multiprocessing.Pool(processes=8)
        filtered_result = pool.map(DataFilterProcessing, dataTotal)
        pool.close()
        pool.join()
        filtered_result = [x for x in filtered_result if x is not None]
    else:
        print("Non-Multi-Process")
        filtered_result = list(d for d in dataTotal if all([ExecuteFilters(d,f["colname"],f["operator"],f["value"]) for f in datafilters]))
    
    print("Filter Time % s seconds" % (time.time() - startFilter))
    return filtered_result