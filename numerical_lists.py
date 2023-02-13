#!/usr/bin/env python

# Creating a numerical list

''' #! Always take the upper value as your value + 1
    To create 1 to 5, your range must be (1, 6)
    You can also use the trick below to put +1 at the end before
    The closing bracket
'''

print("Numbers: ", end='')
print(*range(1, 6), sep=", ")

# list comprehension (one-liner6
print("Even numbers:", ", ".join([str(n) for n in range(2,21,2)]))

squares = [str(nr ** 2) for nr in range(1,11)]
print("Squares:", ", ".join(squares))
