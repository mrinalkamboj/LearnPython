# Decorator are just function that take function as first
# parameter and return a function

def logging(f):
  def decorator_function(*args, **kwargs):
    print('executing '+f.__name__)
    try:
        result = f(*args, **kwargs)        
        return result
    except Exception as e:
        # Log Exception in Fire and Forget Mode
        raise e
  return decorator_function

#Use it like this
@logging
def hello_world():
  print('Hello World')
  raise Exception("Hello World Exception")

result = hello_world()
print(result)