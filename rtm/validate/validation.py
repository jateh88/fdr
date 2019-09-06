"""Each of these functions checks a specific aspect of an RTM field and returns
a ValidationResult object, ready to be printed on the terminal as the final
output of this app."""

# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
# None

# --- Intra-Package Imports ---------------------------------------------------
import rtm.containers.fields
import rtm.validate.checks as checks
from rtm.validate.validator_output import ValidationResult
import rtm.main.context_managers as context


# --- General-purpose validation ----------------------------------------------
def val_column_exist(field_found) -> ValidationResult:
    """Given field_found=True/False, return a ValidationResult, ready to be
    printed to console."""
    title = "Field Exist"
    if field_found:
        score = "Pass"
        explanation = None
    else:
        score = "Error"
        explanation = "Field not found"
    return ValidationResult(score, title, explanation)


def val_column_sort(field_self) -> ValidationResult:
    """Does this field actually appear after the one it's supposed to?"""
    title = "Left/Right Order"

    # --- Field that is supposed to be positioned to this field's left
    field_left = rtm.containers.fields.get_expected_field_left(field_self)

    if field_left is None:
        # argument field is supposed to be all the way to the left.
        # It's always in the correct position.
        score = "Pass"
        explanation = "This field appears to the left of all the others"
    elif field_left.position_right <= field_self.position_left:
        # argument field is to the right of its expected left-hand neighbor
        score = "Pass"
        explanation = (
            f"This field comes after the {field_left.name} field as it should"
        )
    else:
        score = "Error"
        explanation = f"This field should come after {field_left.name}"
    return ValidationResult(score, title, explanation)


def val_cells_not_empty(values) -> ValidationResult:
    """All cells must be non-empty"""
    title = "Not Empty"
    error_indices = []
    for index, value in enumerate(values):
        if checks.cell_empty(value):
            error_indices.append(index)
    if not error_indices:
        score = "Pass"
        explanation = "All cells are non-blank"
    else:
        score = "Error"
        explanation = "Action Required. The following rows are blank:"
    return ValidationResult(score, title, explanation, error_indices)


# --- Cascade Block -----------------------------------------------------------
def val_cascade_block_not_empty():
    """Each row in cascade block must have at least one entry."""
    title = 'Not Empty'
    error_indices = [
        work_item.index
        for work_item in context.work_items.get()
        if work_item.depth is None
    ]
    if not error_indices:
        score = "Pass"
        explanation = "All rows are non-blank"
    else:
        score = "Error"
        explanation = (
            "Action Required. The following rows have blank cascade blocks:"
        )
    return ValidationResult(score, title, explanation, error_indices)


def val_cascade_block_only_one_entry():
    """Each row in cascade block must contain only one entry"""
    title = "Single Entry"
    # indices = []
    # for work_item in context.work_items.get():
    #     _len = len(work_item.cascade_block)
    #     if _len != 1:
    #         indices.append(work_item.index)

    error_indices = [
        work_item.index
        for work_item in context.work_items.get()
        if len(work_item.cascade_block) != 1
    ]
    if not error_indices:
        score = "Pass"
        explanation = "All rows have a single entry"
    else:
        score = "Error"
        explanation = (
            "Action Required. The following rows are blank or have multiple entries:"
        )
    return ValidationResult(score, title, explanation, error_indices)


def val_cascade_block_x_or_f() -> ValidationResult:
    """Value in first position must be X or F."""
    title = "X or F"

    allowed_entries = "X F".split()

    error_indices = [
        index
        for index, work_item in enumerate(context.work_items.get())
        if not checks.values_in_acceptable_entries(
            sequence=[item.value for item in work_item.cascade_block],
            allowed_values=allowed_entries,
        )
    ]

    if not error_indices:
        score = "Pass"
        explanation = f"All entries are one of {allowed_entries}"
    else:
        score = "Error"
        explanation = f"Action Required. The following rows contain something other than the allowed {allowed_entries}:"
    return ValidationResult(score, title, explanation, error_indices)


def val_cascade_block_use_all_columns():
    """The cascade block shouldn't have any unused columns."""
    title = "Use All Columns"

    # Setup fields
    fields = context.fields.get()
    cascade_block = fields.get_field_object('CascadeBlock')
    subfield_count = len(cascade_block)
    positions_expected = set(range(subfield_count))

    # Setup Work Items
    work_items = context.work_items.get()
    positions_actual = set(
        work_item.depth for
        work_item in
        work_items
    )

    missing_positions = positions_expected - positions_actual

    if len(missing_positions) == 0:
        score = "Pass"
        explanation = f"All cascade levels were used."
    else:
        score = "Warning"
        explanation = f"Some cascade levels are unused"

    return ValidationResult(score, title, explanation)


# --- Cascade Level -----------------------------------------------------------
def valid_cascade_levels(field):
    """Check cascade levels against list of acceptable entries."""
    title = 'Valid Entries'
    values = field.values
    error_indices = [
        index
        for index, value in enumerate(values)
        if not checks.cell_empty(value)
           and value not in checks.allowed_cascade_levels.keys()
    ]
    if not error_indices:
        score = "Pass"
        explanation = "All cell values are valid"
    else:
        score = "Error"
        explanation = f'The following cells contain values other than the allowed {checks.allowed_cascade_levels.keys()}:'
    return ValidationResult(score, title, explanation, error_indices)


def val_matching_cascade_levels():
    """A work item's cascade level entry must match its cascade block entry."""
    fields = context.fields.get()
    cascade_level = fields.get_field_object('CascadeLevel')
    title = 'Matching Levels'
    body = cascade_level.values

    # --- Don't report on rows that failed for other reasons (i.e. blank or invalid input
    exclude_results = [
        val_cells_not_empty(body),
        valid_cascade_levels(cascade_level),
        val_cascade_block_not_empty()
    ]
    exclude_indices = []
    for result in exclude_results:
        exclude_indices += list(result.indices)
    indices_to_check = set(range(len(body))) - set(exclude_indices)

    error_indices = []
    work_items = context.work_items.get()
    for index in indices_to_check:
        cascade_block_position = work_items[index].depth
        cascade_level_value = body[index]
        allowed_positions = checks.allowed_cascade_levels[cascade_level_value]
        if cascade_block_position not in allowed_positions:
            error_indices.append(index)

    if not error_indices:
        score = "Pass"
        explanation = "All rows (that passed previous checks) match the position marked in the Cascade Block"
    else:
        score = "Error"
        explanation = f'The following rows do not match the cascade position marked in the Cascade Block:'
    return ValidationResult(score, title, explanation, error_indices)


if __name__ == "__main__":
    pass
