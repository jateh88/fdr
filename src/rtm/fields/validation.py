from typing import List
from rtm.fields.validation_results import ValidationResult


def val_column_sort(correct_position) -> ValidationResult:
    title = "Field Order"
    if correct_position:
        score = 'Pass'
        explanation = None
    else:
        score = 'Error'
        explanation = 'Action Required: Move this column to its correct position'
    return ValidationResult(score, title, explanation)


def val_column_exist(field_found) -> ValidationResult:
    title = "Field Exist"
    if field_found:
        score = 'Pass'
        explanation = None
    else:
        score = 'Error'
        explanation = 'Field not found'
    return ValidationResult(score, title, explanation)


def example_results() -> List[ValidationResult]:
    explanation = 'This is an example explanation'
    examples = [
        ValidationResult('Pass', 'Pass Example', explanation),
        ValidationResult('Warning', 'Warning Example', explanation),
        ValidationResult('Error', 'Error Example', explanation),
    ]
    return examples


def cells_must_not_be_empty(values) -> ValidationResult:
    title = "Not Empty"
    indices = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or not value:
            indices.append(index)
    if not indices:
        score = 'Pass'
        explanation = 'All cells are non-blank'
    else:
        score = 'Error'
        explanation = 'Action Required. The following rows are blank:'
    return ValidationResult(score, title, explanation, indices)


def get_row(index):
    return index + 2


if __name__ == "__main__":
    from collections import namedtuple

    NP = namedtuple("NP", "first second third")
    np = NP('first', 'second', 'third')
    print(np)
    print(None)
