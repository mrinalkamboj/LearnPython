from Filters import ExecuteFilters,FetchFilters # Import Method to Execute the Filters / Fetch the Filters
from DataGenerator import generateData
from Processing import ProcessData
from CustomMemoization import memoize
# from codeprofile import profiler
import time

cnt = 0 

startMain = time.time()

while cnt < len(range(3)):
    
    # Direct Method Call
    dataTotal = generateData(val=1,val1=cnt)

    # Data Filters
    datafilters = FetchFilters()

    print("Total Data Count - ",len(dataTotal))

    # Data Filtering using "and (all)" between filters - ExecuteFilters 
    # We can also use "Or (any)" between the filters   
    
    # # with profiler.profile("FilterTime"):
    filtered_result = ProcessData(dataTotal,datafilters,True)
    
    # # print(filtered_result)

    print("Filter Data Count - ",len(filtered_result))

    # # Code Profiler Time Profiling
    # profiler.print_run_stats("FilterTime")
    
    cnt = cnt + 1

print("Total Time % s seconds" % (time.time() - startMain)) 