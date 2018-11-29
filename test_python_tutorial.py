# A comment, works only for this line
"""This is a quick summary line with no spaces"""

""" 
This is the summary line in a multiline comment

The rest contains the description of a function
    It comments everything between the three quotes
"""

# A word about style: 
# -  Python functions and variables are usually lowercase
# -  A space in a function name or variable contains an underscore
# -  Use multiline quotes for documentation inside functions
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


def quotes():
    # Using quotation marks '' and "", escape with \
    quoth = "\"Always Look on the Bright Side of Life\""
    print(quoth)

    # Or just use quotes
    quoth += '\n"This is a dead parrot!"'
    print(quoth)


def embed_a_string():
    # Embedding a string using %s, which is OG but not great
    print("%s %s %s %s" % ("What", "is", "your", "name?"))

    # Embedding a string using str.format()
    print("What is your {}?".format("quest"))

    # Indexing
    print("What is the {1} of {0} swallow?".format("an unladen", "airspeed velocity"))

    # Advanced, using a dictionary to populate indexes
    words = {'verb': 'floats', 'predicate': 'water'}
    print("What also {verb} in {predicate}?".format(**words))

    # Embedding using F strings, simpler
    name = "Brian"
    age = "boy"
    print(f"The {age} they call {name}")

    # upper or lowercase allowed
    age = "man"
    print(F"The {age} they call {name}")


# Adapted from https://realpython.com/python-f-strings/#option-1-formatting