"""
This script serves as a library of functions for FDR checker. Each function has two comments before it, the first is which
column it is intended for and the second states what it does. unless otherwise stated, each function returns a boolean true or false

"""
# functions start here

# Any
# check if empty. returns True if empty
def is_empty(value):
    if not value:
        return True
    else:
        return False


# Any
# check if value is N/A.
# FDR rules: type of requirement/other circumstances may/may not allow N/A in certain fields
def is_notapplic(value):
    #remove whitespace for direct string comparison. e.g. 'n / a ' becomes 'n/a'
    value = value.replace(" ","")
    #compare lower case version of cell contents to 'n/a'.
    if value.lower() == "n/a":
        return True
    else:
        return False


# Any
# check if value is explicitly a hyphen
# FDR rules: if row is a procedure step, all columns besides ID, cascade visualizer, cascade level and requirement
#   statement should be a hyphen
def is_hypen(value):
    #remove whitespace for direct string comparison. e.g. ' - ' becomes '-'
    value = value.replace(" ","")
    if value == "-":
        return True
    else:
        return False


# Any
# check if value is yes
def is_yes(value):
    #remove whitespace for direct string comparison. e.g. 'yes ' becomes 'yes'
    value = value.replace(" ","")
    if value == "yes":
        return True
    else:
        return False


# Any
# check if value is no
def is_no(value):
    #remove whitespace for direct string comparison. e.g. 'no ' becomes 'no'
    value = value.replace(" ","")
    if value == "no":
        return True
    else:
        return False


# Any
# check if value contains 'not required' in its text
# FDR rules: some fields are not required. e.g. validation is not required if requirement is a business need
def has_not_required(value):
    if value.lower().find("not required") != -1:
        return True
    else:
        return False


# ID
# check that value has a capital P as the first character.
# FDR rules: recommended ID formatting for procedure steps and procedure based requirements follow a naming convention.
#   e.g. P010, P020, etc. for procedure steps and P010-020 for procedure based requirements
def starts_with_p(value):
    if value.startswith("P"):
        return True
    else:
        return False


# ID
# check if value has integers following the first letter
# FDR rules: recommended ID formatting for procedure steps follow a naming convention.
#   e.g. P010, P020, etc. for procedure steps
def has_digits_after_first(value):
    return value[1:].isdigit()


# ID
# check if value has 3 integers following the first character. First char is omitted
# FDR rules: recommended ID formatting for procedure steps follow a naming convention.
#   e.g. P010, P020, etc. for procedure steps
def has_three_digits(value):
    str1 = value[1:]
    if (len(str1) == 3) and (str1.isdigit() == True):
        return True
    else:
        return False


# ID
# check if value has 6 integers following the first character.
# FDR rules: recommended ID formatting for procedure based requirements follow a naming convention.
#   e.g. P010-020, P010-030, etc. for procedure based requirements
# NOTE: First char is omitted. Assumes there is a dash and removes it
def has_six_digits(value):
    #slice string. keep all characters after the first. (removes P)
    value_slice = value[1:]
    #find the location/index of the hypen within the string.
    dash_index = value_slice.find("-")
    #slice string around the hyphen. this will leave only the numeric characters if ID if formatted correctly
    value_slice = value_slice[:dash_index] + value_slice[dash_index + 1:]
    if (len(value_slice) == 6) and (value_slice.isdigit() == True):
        return True
    else:
        return False


# ID
# check for hyphen within string
# FDR rules: recommended ID formatting for procedure based requirements follow a naming convention.
# e.g. P010-020, P010-030, etc. for procedure based requirements
def has_hyphen(value):
    if value.find("-") != -1:
        return True
    else:
        return False


# ID
# Check for dash in 4th position (P010-001)
# FDR rules: recommended ID formatting for procedure based requirements follow a naming convention.
# e.g. P010-020, P010-030, etc. for procedure based requirements
def has_hyphen_positioned(value):
    if value.find("-") == 4:
        return True
    else:
        return False


# Cascade Block
# check for capital X
# FDR rules: only a capital X or capital F are allowed in the cascade visualizer columns. (B-G in its current form)
def has_capital_x(value):
    #remove whitespace for direct string comparison. e.g. ' X ' becomes 'X'
    value = value.replace(" ","")
    if value == "X":
        return True
    else:
        return False


# Cascade Block
# check for lowercase x
# FDR rules: only a capital X or capital F are allowed in the cascade visualizer columns. (B-G in its current form)
def has_lower_x(value):
    #remove whitespace for direct string comparison. e.g. ' x ' becomes 'x'
    value = value.replace(" ","")
    if value == "x":
        return True
    else:
        return False


# Cascade Block
# check for capital F
# FDR rules: only a capital X or capital F are allowed in the cascade visualizer columns. (B-G in its current form)
def has_capital_f(value):
    #remove whitespace for direct string comparison. e.g. ' F ' becomes 'F'
    value = value.replace(" ","")
    if value == "F":
        return True
    else:
        return False


# Cascade Block
# check for lowercase f
# FDR rules: only a capital X or capital F are allowed in the cascade visualizer columns. (B-G in its current form)
def has_lower_f(value):
    #remove whitespace for direct string comparison. e.g. ' f ' becomes 'f'
    value = value.replace(" ","")
    if value == "f":
        return True
    else:
        return False


# Cascade level
# check if cascade level is 'procedure step'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_procedure_step(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "procedure step":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'user need'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_user_need(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "user need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'risk need'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_risk_need(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "risk need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'business need'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_business_need(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "business need":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'design input'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_design_input(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "design input":
        return True
    else:
        return False


# Cascade Level
# check if cascade level is 'design output solution'
# FDR rules: cascade level defines the type of requirement and can only contain one of the following strings:
# procedure step, user need, risk need, business need, design input or design output
def is_design_output(value):
    #remove whitespace at the beginning and end of the string and test for value
    if value.strip().lower() == "design output solution":
        return True
    else:
        return False


# Cascade level
# check if cascade level is one of the approved options.
# returns true if it is procedure step, user need, risk need, business need, design input or design output
def is_cascade_lvl_approved(value):
    if is_procedure_step(value) ^ is_user_need(value) ^ is_risk_need(value) \
            ^ is_business_need(value) ^ is_design_input(value) ^ is_design_output(value) == True:
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


# V&V
# check if windchill number is present

"""
SANDBOX 
"""
if __name__ == '__main__':

    # This is your playground
    # call function
    # print result

    testval = "P010"
    testout = is_business_need(testval)
    print(testout)
    pass

    """

# init a mock requirement (row on FDR) for testing
req1 = dict(iD="P20", procedureStep=" ", userNeed="X", cascadeLevel="DESIGN OUTPUT SOLUTION",
            requirementStatement="Prepare Patient")
print("\n")
print(req1)
print("\n")

"""