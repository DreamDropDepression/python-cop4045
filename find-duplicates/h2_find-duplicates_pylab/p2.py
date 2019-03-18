# Problem 2 - Duplicate strings
'''
User enters a string, program looks for duplicates of size n
Teacher's solution used a utility function "find_substring"
'''
import math


def find_dup_str(s, n):
    '''Returns the substrings of size n across s.
       I tried to minimize creating placeholder variables
    '''
    str_lst = []
    for i in range(0, len(s) - n + 1):
        if s[i:i+n] in str_lst:
            return s[i:i+n]
        else:
            str_lst.append(s[i:i+n])
    return ""


def find_max_dup(s):
    '''half the len() is the biggest possible string'''
    dmax = ""
    for n in range(2, math.ceil((len(s)/2))):
        ss = find_dup_str(s, n)
        if ss == "":
            continue
        elif ss > dmax:
            dmax = ss
    return dmax


def main():
    '''Initialize Values before caring about input'''
    in_str = input("Enter text, then press <ENTER>: ")
    n = int(input("Enter an integer for string-size: "))
    print("s =", in_str, "\nn =", n)
    print(find_dup_str(in_str, n))
    s = 'abcgdefbczdgz'
    s2 = 'abcdefbcdgh'
    s3 = 'abcdefabcdghabcd'
    s4 = 'abchfurijdjfurabcpqweabc'
    print(find_max_dup(s))
    print(find_max_dup(s2))
    print(find_max_dup(s3))
    print(find_max_dup(s4))


main()
