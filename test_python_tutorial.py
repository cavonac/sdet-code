# A comment, works only for this line


""" This is a multiline quote
    It comments everything between the three quotes
"""

# A word about style: 
# -  Python functions and variables are usually lowercase
# -  No one uses multiline quotes except for documentation inside functions
# -  Python is whitespace sensitive! 
# -  Definitions blocks are followed by double lines, such as this:


def python_simple_operators():
    # Python simple operators
    print("Addition: 5 + 3 = ", 5+3)
    print("Subtraction: 5 - 3 = ", 5-2)
    print("Multiplication: 5 * 2 = ", 5*2)
    print("Division: 5 / 2 = ", 5/2)


def python_interesting_operators():
    # Python interesting operators
    print("Modulo: 5 % 3 = ", 5%3)
    print("Exponential: 5 ** 3 =", 5**3)
    print("Floor Division: 5 // 3 = ", 5//3)


def python_order_of_operations():
    # Order of operations are typical, * and / before + and -
    print("5 + 3 * 2 + 4 / 2 = ", 5 + 3 * 2 + 4 / 2)
    print("5 + 3 * (2 + 4) / 2", 5 + 3 * (2 + 4) / 2)


# Using quotation marks '' and "", escape with \
quoth = "\"Always Look on the Bright Side of Life\""
print(quoth)


# Or just use quotes
quoth += '\n"This is a dead parrot!"'
print(quoth)


# Embedding a string


# Adapted from https://youtu.be/N4mEzFDjqtA