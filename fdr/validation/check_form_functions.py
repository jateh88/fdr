"""
This script serves as a library of functions for FDR checker. Each function has two comments before it, the first is which
column it is intended for and the second states what it does. unless otherwise stated, each function returns a boolean true or false



# init a mock requirement (row on FDR) for testing
req1 = dict(iD="P20", procedureStep=" ", userNeed="X", cascadeLevel="DESIGN OUTPUT SOLUTION", requirementStatement= "Prepare Patient")
print("\n")
print(req1)
print("\n")


"""
# functions start here

# Any
# check if not empty. returns True if not empty
# a.k.a true if value is a string
def not_empty(value):
    if not value:
        return False
    else:
        return True

# Any
# check if value is N/A
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
# check if value is yes
def is_yes(value):
    if value == "yes":
        return True
    else:
        return False

# Any
# check if value is no
def is_no(value):
    if value == "no":
        return True
    else:
        return False

# Any
# check if value contains 'not required' in its text
def has_notrequired(value):
    if value.lower().find("not required") != -1:
        return True
    else:
        return False

# ID
# check that value has a capital P as the first character.
def startswith_p(value):
    if value.startswith("P"):
        return True
    else:
        return False

# ID
# check if value has integers following the first letter (follows numbering scheme P010, P020, etc.)
def has_digitsafterfirst(value):
    return value[1:].isdigit()

# ID
# check if value has 3 integers following the first character. First char is omitted
def has_threedigits(value):
    str1=value[1:]
    if (len(str1) == 3) and (str1.isdigit() == True):
        return True
    else:
        return False

# ID
# check if value has 6 integers following the first character.
# NOTE: First char is omitted. Assumes there is a dash and removes it
def has_sixdigits(value):
    str1=value[1:]
    dash = str1.find("-")
    str1=str1[:dash]+str1[dash+1:]
    if (len(str1) == 6) and (str1.isdigit() == True):
        return True
    else:
        return False

# ID
# check for hyphen within string
def has_hyphen(value):
    if value.find("-") != -1:
        return True
    else:
        return False

# ID
# Check for dash in 4th position (P010-001)
def has_hyphen_positioned(value):
    if value.find("-") == 4:
        return True
    else:
        return False

# Cascade Block
# check for capital X
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

# Cascade level
# check if cascade level is one of the approved options.
# returns true if it is procedure step, user need, risk need, business need, design input or design output
def is_cascadelvl_approved(value):
    if is_procedure(value) ^ is_user_need(value) ^ is_risk_need(value) \
            ^ is_busi_need(value) ^ is_design_input(value) ^ is_design_output(value) == True:
        return True
    else:
        return False

# V&V Results
# check if W/C,wc or windchill is present. should indicate if windchill number is present
def has_w_slash_c(value):
    if value.lower().find("w/c") != -1:
        return True
    elif value.lower().find("wc") != -1:
        return True
    elif value.lower().find("windchill") != -1:
        return True
    else:
        return False


# V&V !!IN WORK!!
# check if windchill number is a valid WC number by counting the digits. example W/C# 0000006634
def is_windchill_valid(value):
    # find index of 000. windchill numbers have at least three leading zeros.
    index = value.find("000")
    #slice the string starting at that index until the end of the string
    value = value[index:]
    #remove all spaces
    value = value.replace(" ", "")

    # test if rest of string is only digits. if all digits, count the number of digits and return true if there are 10
    if (value.isdigit() == True) and (len(value)==10): #FIX! length doesnt have to be 10
        return True
    # If not all digits, slice the string after 10
    value = value[9:]
    # check if the rest of the string is letters only. this means WC# is correct. return true digits.
    if value.isalpha()==True:
        return True
    #else... (alpha numeric or digits) return false.
    else:
        return False




# Design Output Feature
# check for any ctq IDs


if __name__ == '__main__':
    #This is your playground
    #call function
    #print result

    testval = "# 0000000000 blah blah blah"
    testout = has_w_slash_c(testval)
    print(testout)
    pass