# exception handling quick intro

# exception are errors that occur during the execution of a program

# Basic except. handling using try, except and optionally, finally
try:
    # code that raises exception
    x = 10 / 0
except ZeroDivisionError:   # SomeException
    print("You cannot divide by zero!")
    