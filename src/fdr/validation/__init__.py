# TODO pseudocode for validated excel content:
"""
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
Check Headers
    Cells in first row = headers
    Start with a tuple of all the headers (this is a solid, unmutable baseline that can be used in other operations)
    Add each header_actual to collection.Counter object (this will highlight any non-unique headers)
    For each header_required:
        check the counter. If count ==1, good.
        elif count == 0, header not found
        if count < 0, we made a programming error
        if count > 1, a required header is non-unique. Handle the error; print.
    Question: How do we handle variable headers? Example: variable number of design output headers?
        Does this require an approach different than the counter strategy?
    Question: we care about the headers sequence, right?
        Do we care if there's an extra column thrown in? Probably not. But maybe we throw a warning.

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
