"""
This script serves as a library of functions for FDR checker. Each function has two comments before it, the first is which
column it is intended for and the second is what it does. unless otherwise stated, each function returns a boolean true or false

"""

# TODO - Jonathan notes
#   1. Note how writing "TODO" in a comment line highlights the text.
#      You can also view all the TODOs in a project or file. Just a useful FYI.
#   2. Feel free to delete my comments as you work through them.
# TODO - Jonahtan Notes - FYI: look into refactoring if you're not familiar with it already.
#   It allows you to move or rename function/variables/etc without breaking the code that references it.
#   This will


# TODO Jonathan Notes - this would fit better in the sandbox at the bottom.
# init a mock requirement (row on FDR) for testing
req1 = dict(iD="P20", procedureStep=" ", userNeed="X", cascadeLevel="DESIGN OUTPUT SOLUTION",
            requirementStatement="Prepare Patient")
print("\n")
print(req1)
print("\n")


# functions start here

# Any
# check if not empty. returns True if not empty
# a.k.a true if value is a string
# TODO Jonathan Note: Best practice: boolean functions should be phrased as positive. Here: 'is_empty'.
#   This prevents awkward possible double negatives where this function is called.
def not_empty(value):
    if not value:
        return False
    else:
        return True


# Any
# check if value is N/A
# TODO Jonathan Notes - I'm not sure how best to approach this right now, but do we care if there's whitespace
#   in the value, e.g. '  n/a'
# TODO Jonathan Notes - take a quick look at PEP 8. It describes python code formatting.
#   Example: 2 empty lines between functions.
def is_notapplic(value):
    if value.lower() == "n/a":
        return True
    else:
        return False


# Any
# check if value is explicitly a hyphen
def is_hypen(value):
    if value == "-":
        return True
    else:
        return False


# Any
# check if value contains 'not required' in its text
def has_notrequired(value):
    # TODO Jonathan Notes - Best practice: variable names should be descriptive and generally not end in a digit.
    #   Alternatives: 'string_', 'lower_case', 'lower_case_string', or just value.lower().find(....)
    str1 = value.lower()
    if str1.find("not required") != -1:
        return True
    else:
        return False


# ID
# check that value has a capital P as the first character.
# TODO Jonathan Note: Best Practice: explain *why* this function does what it does.
#   Here especially, it's clear that you're looking to see if it starts with P.
#   What the reader doesn't know is why we care about this.
#   Better function name: 'starts_with_p'. This comment applies to the next several functions as well.
#   This is just a Python convention.
def startswith_p(value):
    if value.startswith("P"):
        return True
    else:
        return False


# ID
# check if value has integers following the first letter (follows numbering scheme P010, P020, etc.)
def has_digitsafterfirst(value):
    str1 = value[1:]
    return str1.isdigit()


# ID
# check if value has 3 integers following the first character. First char is omitted
def has_threedigits(value):
    str1 = value[1:]
    if (len(str1) == 3) and (str1.isdigit() == True):
        return True
    else:
        return False


# ID
# check if value has 6 integers following the first character.
# NOTE: First char is omitted. Assumes there is a dash and removes it
def has_sixdigits(value):
    str1 = value[1:]
    dash = str1.find("-")
    str1 = str1[:dash] + str1[dash + 1:]
    if (len(str1) == 6) and (str1.isdigit() == True):
        return True
    else:
        return False


# ID
# check for hyphen within string
def has_hyphen(value):
    dash = value.find("-")
    if dash != -1:
        return True
    else:
        return False


# ID
# Check for dash in 4th position (P010-001)
# TODO Jonathan Notes - you're probably going to get around to this, but we'll need higher-order functions for this.
#   Example: a single function that checks the format of the entire string.
#   Another function might compare the current row's string comes alphabetically after the previous row's.
def has_hyphen_positioned(value):
    dash = value.find("-")
    if dash == 4:
        return True
    else:
        return False


# Cascade Block
# check for capital X
# TODO Jonathan Notes - a better function might look for the position of the X in the row.
def has_capital_x(value):
    if value == "X":
        return True
    else:
        return False


# Cascade Block
# check for lowercase x
def has_lower_x(value):
    if value == "x":
        return True
    else:
        return False


# Cascade Block
# check for capital F
def has_capital_f(value):
    if value == "F":
        return True
    else:
        return False


# Cascade Block
# check for lowercase f
def has_lower_f(value):
    if value == "f":
        return True
    else:
        return False


# Cascade level
# check if cascade level is 'procedure step'
def is_procedure(value):
    if value.lower() == "procedure step":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'user need'
def is_user_need(value):
    if value.lower() == "user need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'risk need'
def is_risk_need(value):
    if value.lower() == "risk need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'business need'
def is_busi_need(value):
    if value.lower() == "business need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'design input'
def is_design_input(value):
    if value.lower() == "design input":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'design output solution'
def is_design_output(value):
    if value.lower() == "design output solution":
        return True
    else:
        return False


# V&V
# check if windchill number is present

# V&V
# check if windchill number is accurate

if __name__ == '__main__':
    # This is your playground
    # call function
    # print result

    testval = "blah blah blah not required"
    testout = hasNotReq(testval)
    print(testout)
    pass
