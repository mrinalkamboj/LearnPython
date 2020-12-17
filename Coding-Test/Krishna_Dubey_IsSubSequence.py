def process_subarray(A,B):
    n = len(A)
    m = len(B)
    i = 0 
    j = 0 
    
    reverse = 0
    sub = 0
    while (i < n and j < m): 
        if (A[i] == B[j]): 
            i += 1 
            j += 1 
            if (j == m): 
                sub = 1
                break
        else: 
            i = i + 1

    B = B[::-1] 
    i = 0
    j = 0    
    while (i < n and j < m): 
        if (A[i] == B[j]): 
            i += 1 
            j += 1 
            if (j == m): 
                reverse = 1
                break
        else: 
            i = i + 1
    
    return(sub,reverse)
        
    
def check_subarray(m,l):
    print('\n')
    print("main array: ",m)
    print("sub array: ", l)
    
    sub,reverse = process_subarray(m,l)
    if sub|reverse == 0:
        print('Sequence is not a Sub Array of Main Array')
    elif sub&reverse == 1:
        print("Sequence is Bi-directional Sub Array of Main Array")
    elif sub == 1:
        print("Sequence is Sub Array of Main Array")
    else:
        print("Sequence is Reverse Sub Array of Main Array")
        
    
m = [1,3,5,7,9,11]   
#1st case
check_subarray(m,[1,5,11])
# # #2nd case
# # check_subarray(m,[7,5,1])
# # #3rd case
# # check_subarray(m,[1])
# # #4th case
# # check_subarray(m,[2,4,6])






