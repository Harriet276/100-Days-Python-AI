from datetime import datetime
from fcntl import FASYNC  ##  Day 12: Decorators  ##
###  Outcome: Learn how to modify or extend a function’s behavior without changing its actual code ###


## Practice Question ##

# Create a decorator that prints:
# "Start function" before running
# "End function" after running
# Apply it to a greeting function.


def trial_decorator(func):
     def wrapper():
         print("Start function")
         func()
         print("End function")
     return wrapper

@trial_decorator
def greeting():
    print(f"Hello, Harriet \n How are you today?")

# greeting()


### Practice Question #2 ###
# Create a decorator that only allows the function to run once per session.
def has_run(func):
    has_run = False
    def  wrapper(*args, **kargs):
        nonlocal  has_run
        if not has_run:
            print("This is the first time the function is running")
            has_run = True
            return  func(*args, **kargs)
        else:
            print("FUnction already run once skipping now")
    return wrapper


@has_run
def test_function():
    print("Greetings")


# test_function()
# test_function()

### Practice Question #3 ###
#Write a decorator that logs the name and time of each function call.
def log_decorator(func):
    def wrapper(*args):
        print(func.__name__)
        print(datetime.now())
        return func(*args)
    return wrapper

@log_decorator
def function():
    print('Success')

# function()

### Practice Question #4 ###
# Create a decorator that capitalizes the return string of a function

def log_operator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
@log_operator
def function1():
    return "asaaaswaaabaabababab"

print(function1())
