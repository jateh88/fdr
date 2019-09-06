"""Whereas the validation functions return results that will be outputted by
the RTM Validator, these "checks" functions perform smaller tasks, like
checking individual cells."""

# --- Standard Library Imports ------------------------------------------------

# --- Third Party Imports -----------------------------------------------------
# None

# --- Intra-Package Imports ---------------------------------------------------


def cell_empty(value) -> bool:
    """Checks if a cell is empty. Cells contain True or False return False"""
    if isinstance(value, bool):
        return False
    if not value:
        return True
    return False


def values_in_acceptable_entries(sequence, allowed_values):
    """Each value in the sequence must be an allowed values. Otherwise, False."""
    if len(sequence) == 0:
        return True
    for item in sequence:
        if item not in allowed_values:
            return False
    return True


# I would like to have included this variable in the CascadeLevel, but that
# would cause circular references.
allowed_cascade_levels = {  # keys: level, values: position
        'PROCEDURE STEP': [0],
        'VOC USER NEED': [1],
        'BUSINESS NEED': [1],
        'RISK NEED': [1],
        'DESIGN INPUT': [2],
        'DESIGN OUTPUT SOLUTION': list(range(3, 20))
    }
