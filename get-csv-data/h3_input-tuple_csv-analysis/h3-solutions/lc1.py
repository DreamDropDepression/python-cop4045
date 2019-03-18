# Python Course

# examples with list comprehensions

# the expression for list lst:
#   lst = []
#   for x in <iterable>:
#      x.append(<exp>)
#
# is equivalent with a LC of the form:
#   lst = [ <exp> for x in <iterable>]


# create list with squares, the normal way:
lst = []     # start with empty list:
for i in range(0,101):
    lst.append(i**2)

#print(lst)

# with a lc:
lst = [ i**2 for i in range(0,101) ]

#print(lst)

# --------------------------------------------------------------------

# the expression for list lst with a filter <cond> (logical condition):
#   lst = []
#   for x in <iterable>:
#      if <cond>:
#         x.append(<exp>)
#
# is equivalent with a LC of the form:
#   lst = [ <exp> for x in <iterable> if <cond>]


# list with squares of even numbers:
lst = []
for i in range(0,101):
    if i % 2 == 0:
        lst.append(i**2)

#print(lst)

# with list comprehension:
lst = [ i**2 for i in range(0,101) if i % 2 == 0 ]
#print(lst)

# --------------------------------------------------------------------

# with two iterables:

# the expression for list lst a nested for loop:
#   lst = []
#   for x in <iterable1>:
#      for y in <iterable2>:
#         x.append(<exp>)
#
# is equivalent with a LC of the form:
#   lst = [ <exp> for x in <iterable1> for y in <iterable2>]


# create a list with all possible elements of Carthesian product (1..4)x(1..4):
lst = []
for i in range(1,5):
    for j in range(1,5):
        lst.append((i,j))

#print(lst)

# equivalent lc:
lst = [ (i,j) for i in range(1,5) for j in range(1,5)]
#print(lst)

# --------------------------------------------------------------------

# the expression for list lst with a nested for loop:
# with two iterables and a filter condition:
#   lst = []
#   for x in <iterable1>:
#      for y in <iterable2>:
#         if <cond>:
#            x.append(<exp>)
#
# is equivalent with a LC of the form:
#   lst = [ <exp> for x in <iterable1> for y in <iterable2> if <cond>]


# ... same as before, with i+j= 4
lst = [ (i,j) for i in range(1,5) for j in range(1,5) if i+j==4]
#print(lst)


# --------------------------------------------------------------------

# The Python Conditional Expression:

# Similar to the ?: ternary operator in C/C++/Java:
# Expression
#    <exp1> if <cond> else <exp2}
# is evaluated in the following way:
# 1. <cond> is evaluated
# 2. if <cond> == True, then <exp1> is evaluated and the value of
#    the conditional expression is the value of <exp1>
# 3. if <cond> == False, then <exp2> is evaluated and the value of
#    the conditional expression is the value of <exp2>

# examples:

yesno = 'yes' if input("Enter y/n ") == "y" else 'no'
print("yesno == ",yesno)

a, b = 3.0, -6.0

x = (-b / a) if a != 0 else None    # solution to linear eq. x<--None if a==0


# using conditional expression with list comprehension:
# generate list of pairs (-i,j) if i is even or (i,j) if i is odd
lst = []
for i in range(1,5):
    for j in range(1,5):
        if i % 2 == 0:
            val = -i
        else:
            val = i
        lst.append((val,j))
print(lst)


# with lc:
lst = [((-i,j) if i%2==0 else (i,j)) for i in range(1,5) for j in range(1,5) ]
print(lst)


