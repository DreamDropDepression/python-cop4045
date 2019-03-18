# Python class. Chapter 6 Files & exceptions.
# Demonstrate exceptions.

# avoid duplicating code by defining a function for inspecting
# the error object:
def print_error(er):
    print("Exception type: {} : the error message was '{}'.".format(type(er), er))
    

# main program
# checking valid input to avoid parsing error or divide-by-0 error:
try:
    # solve linear equation ax+b=0
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))

    # if parsing to float fails we never get to this point:
    # optimistically assume a!=0
    x = -b / a
    print("The solution is {}.".format(x))

except ValueError as er:
    # obtain a reference to the error object and inspect it    
    # parsing failed:
    print_error(er)
except ZeroDivisionError as er:
    print_error(er)
except:
    # catch-all for any other exception types:  should not happen here
    print("Unexpected error type.")    
finally:
    print("\nIn the finally block -- this is printed regardless of exceptions")


print("The main program ends now.")
    
