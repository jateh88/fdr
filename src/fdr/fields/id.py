from .field import Field
import click
# TODO added click module for click.echo.

class ID(Field):

    __header_name_seq = ['ID']

    # TODO Note to Jonathan- I'm not sure if it makes sense to define the validation function here or in validate().
    #  I copied/pasted it from check_form_functions.py and is called below in the body of validate().
    # Define validation functions (for demonstration, checking that the value starts with P will be the only one)
    # Targeted column: ID
    # What it does: checks that value has a capital P as the first character.
    # FDR rules: recommended ID formatting for procedure steps and procedure based requirements follow a naming
    # convention. e.g. P010, P020, etc. for procedure steps and P010-020 for procedure based requirements
    def starts_with_p(value):
        if value.startswith("P"):
            return True
        else:
            return False

    # TODO Note to Jonathan- I have tested the body of validate() assuming "self" is a list of strings but
    #  haven't tested by calling it as a method
    def validate(self):
        # Currently, validate() will only check if a value starts with P and will print a descriptive message when
        # called. the input argument defined is a list of IDs that was previously extracted from the FDR.
        # Init. an empty list that will contain the spreadsheet rows where discrepancies are found
        error_indeces = []
        # for indeces (location of errors) and ids (value in cell) in self (input argument) enumerate list starting
        # with 1. This will offset indeces so it can be used to directly reference excel sheet (row#)
        for indeces, ids in enumerate(self, 1):
            # call validation function to check value and compare to boolean
            if starts_with_p(ids) is False:
                # if discrepancy found (validation function is false), append the index to a list
                error_indeces.append(indeces)
        # Determine the length of the error_indeces list. this is indicative of the number of errors.
        # call constructor function (str()) to cast string for output
        error_count = str(len(error_indeces))
        # call str() to cast the indeces to string for output
        error_rows = str(error_indeces)
        output_string = "Discrepancy Description: ID does not start with P. Discrepancy count: " + error_count + \
                        ". Found in in Rows: " + error_rows
        click.echo(output_string)
        # Other validation actions (future state)
        # - column exists
        # - cells not empty
        # - cells in alphabetical order
