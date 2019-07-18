from .field import Field
from .id import ID
from .devices import Devices

# The ordering for the excel fields will be evaluated according to the order given here.
field_class_seq = [
    ID,
    Devices,
]

pseudocode = """
User types 'fdr' into command prompt
    (Later, there will be other options. For now, this is what's planned)
Get path
    If path exist in db:
        get the last three, starting with most recent
        use click.prompt to have user pick b/w one of these three or selecting a new one.
    else:
        have user select a new one.
    If path not exist, throw fnf error
    If path not ends in .xls or .xlsx, throw valuerror
    Add selected path to db
        delete it from the db if it already exists
        Add the new one to db. This should be on its own table.
Check Headers: existence and col #
    Get list of headers
        Cells in first row = headers
        Start with a tuple of all the headers (this is a solid, unmutable baseline that can be used in other operations)
    Get list of fields (objects)
    For each field,
        pass the headers list to the field object
        That object checks the header list for its name and records matching column number(s) in a list.
            Some fields will check for multiple headers, like the DI/DO field
        If column number count == 1, good
        elif > 1, we have duplicates. Print this?
        else: header not found. Print this.
        object returns list of column numbers
    At this point, each field knows which columns it gets its cell values from.
        It also knows if there are header dups or if the column is missing entirely.
        Future feature: If missing, seek most similar string.
        If we do this though, we'll have to be careful not to have two+ fields select the same row.
        We'd have to mark columns as "taken".
Check header sequence
    For each field:
        pass in col num of previous field (the first field will be given a zero)
        object: assert self col num > argument
        Print if fail
Pass cell data to objects
    For each field:
        pass seq of all cell data
Validate cell values
    For each field:
        If header exists:
            validate cell values.
            'validate' will be a class(?) method that calls the needed functions.

    ...

Each column (or column group like DI/DO) gets its own class
Class data:
    Header name(s)
    column number
    list (or tuple) of cell values
Instance data:
    row number
Class methods:
    not empty (base class)
    alphabetical order
    exists

"""
