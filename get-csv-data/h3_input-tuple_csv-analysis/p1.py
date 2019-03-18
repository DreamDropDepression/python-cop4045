# Problem 1 Input Tuple
'''Reads strings from user or a file, then uses a tuple to typecast each item
    Parameters:
        prompt: string for input prompt
        types: a tuple of types that match user input
        sep: separator used in parsing the user input. Defaule = ","
'''
from testif import testif

# function will pass these variables containing expected values
prompt_str = "Enter first name, last name, Age, ID, Fulltime(y/n or leave blank)\
              separate items with ','\n   > "
types_tup = (str, str, float, int, bool)
car_types_tup = (str, str, float, int)

def cast(typ, item):
    """Returns the typed value of the item string"""
    if typ == bool:
        if item.lower() != 'y' or item.strip() == "":
            return False
        else:
            return True
    return typ(item)

def input_tuple(prompt, types, sep=','):
    """Success: Returns converted values. Failure: Returns empty tuple"""

    word_list = input(prompt).split(sep)
    if len(word_list) != len(types):
        print("Error: Number of items entered is not equal to number of types to parse")
        return ()

    try:
        typed_list = []
        for i, word in enumerate(word_list):
            typed_list.append(cast(types[i], word.strip()))
        return tuple(typed_list)

    except ValueError:
        print("Error: Parsing strings failed")
        return ()

def input_tuple_lc(prompt, types, sep=","):
    """Same as input_tuple but using list comprehension"""
    word_list = input(prompt).split(sep)
    if len(word_list) != len(types):
        print("Error: Number of items entered is not equal to number of types to parse")
        return ()

    try:
        return tuple([cast(types[i], word.strip()) for i, word in enumerate(word_list)])

    except ValueError:
        print("Error: Parsing strings failed")
        return ()

def convert(string, types, sep=","):
    """Works like input_tuple_lc without the input function"""
    word_list = string.split(sep)
    if len(word_list) != len(types):
        print("Error: Number of items entered is not equal to number of types to parse")
        return ()

    try:
        return tuple([cast(types[i], word.strip()) for i, word in enumerate(word_list)])

    except ValueError:
        print("Error: Parsing strings failed")
        return ()

def read_tuple(file_obj, types, sep=","):
    """Same as input_tuple but reades input from a file."""
    line = file_obj.readline()
    return convert(line, types, sep)

def read_list_of_tuples(f_obj, typs, sep=','):
    """Returns a list of tuples rather than just one"""
    car_vals = []
    for line in f_obj:
        if len(line.split(sep)) != len(typs):
            return ()
        car_vals.append(tuple([typ(el) for typ, el in zip(typs, line.rstrip('\n').split(sep))]))
    return car_vals

def test_input_tuples():
    '''Testing functions that don't read from file'''
    student_tuple = input_tuple(prompt_str, types_tup, ',')
    testif(student_tuple == ('Dan', 'Pettus', 27.0, 2332, True), "input_tuple"\
            , "input_tuple passed", "input_tuple failed")

    student_tuple_lc = input_tuple_lc(prompt_str, types_tup, ',')
    testif(student_tuple_lc == ('Dan', 'Pettus', 27.0, 2332, False), "input_tuple_lc"\
            , "input_tuple_lc passed", "input_tuple_lc failed")

    # Test for failures
    testif(student_tuple == ('Dan', 'Pettus', 27.0, 2332, True), "input_tuple"\
            , "input_tuple passed", "input_tuple failed")
    testif(student_tuple_lc == ('Dan', 'Pettus', 27.0, 2332, False), "input_tuple_lc"\
            , "input_tuple_lc passed", "input_tuple_lc failed")

def test_read_files():
    '''Test: returns 1 tuple per call'''
    fin = open("cars.csv", "r")
    car1 = read_tuple(fin, car_types_tup, ",")
    car2 = read_tuple(fin, car_types_tup, ",")
    fin.close()
    testif(car1 == ('Lada', 'Niva', 19.5, 1987) and car2 == ('Porsche', '911 Turbo S', 17.5, 1989)\
        , 'read_tuple', 'read_tuple passed', 'read_tuple failed')

    fin = open("cars.csv", "r")
    car_list = read_list_of_tuples(fin, car_types_tup, ',')
    testif(car_list == [('Lada', 'Niva', 19.5, 1987), ('Porsche', '911 Turbo S', 17.5, 1989)]\
        , 'read_list_of_tuples', 'read_list_of_tuples passed', 'read_list_of_tuples failed')
    fin.close()

    # Failed Tests
    fin = open("cars_fail.csv", "r")
    car1 = read_tuple(fin, car_types_tup, ",")
    car2 = read_tuple(fin, car_types_tup, ",")
    fin.close()
    testif(car1 == ('Lada', 'Niva', 19.5, 1987) and car2 == ('Porsche', '911 Turbo S', 17.5, 1989)\
        , 'read_tuple', 'read_tuple passed', 'read_tuple failed')

    fin = open("cars_fail.csv", "r")
    car_list = read_list_of_tuples(fin, car_types_tup, ',')
    testif(car_list == [('Lada', 'Niva', 19.5, 1987), ('Porsche', '911 Turbo S', 17.5, 1989)]\
        , 'read_list_of_tuples', 'read_list_of_tuples passed', 'read_list_of_tuples failed')
    fin.close()

def test_read_list_of_tuples():
    '''Test: returns list of tuples'''
    f_obj = open("cars.csv", "r")
    print(read_list_of_tuples(f_obj, car_types_tup, ','))
    f_obj.close()

def main():
    """Main Function"""
    test_input_tuples()
    test_read_files()

main()
