# Python class. Chapter 6 Files & exceptions.
# Illustration of exception handling when using files and parsing.

# assume file has format "10 3 -5 10.3"
def average_file(filename):
    '''Compute the average  of all numbers from a file.
    This function is not practical as it returns a special value
    in case of errors instead of raising exceptions itself,
    which is the right way of dealing with errors.
    '''
    try:
        f = None     # define f in case open() fails. Needed in 'finally'.
        f = open(filename, "r")
        s = 0.0
        count = 0
        for line in f:
            for tok in line.split():
                s = s + float(tok)
                count = count + 1
                
        return s / count       # the finally block will run before any 'return'
    except ValueError:
        print("error: parse error (ValueError): ", tok)
        return 0
    except ZeroDivisionError:
        print("error: division by zero")
        return 0
    except FileNotFoundError:
        print("error: file not found")
        return 0
    except PermissionError:
        print("error: no permission to open file")
        return 0
    finally:
        # a finally block is the recommended place to close the file.
        print("In the finally suite. Close the file.")
        if f:            # if open failed then f remained None
            f.close()

# pass a bad file name to experience with FileNotFoundError exception.
# pass an empty file to experience with ZeroDivisionError exception.
# or have bad format to trigger ValueError.
avg = average_file("data.txt")
if avg != 0:
    print("In main: average is {}.".format(avg))
else:
    print("In main: some error ocurred.")
