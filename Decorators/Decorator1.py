def hello_decorator(func): 
    def inner1(*args, **kwargs): 
          
        print("Begin Hello Decorator") 
          
        # getting the returned value 
        returned_value = func(*args, **kwargs) 

        print("End Hello Decorator") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a,b,c): 
    print("Inside the function") 
    return a + b + c
  
a, b,c = 1,2,4
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b,c)) 
