def val_column_sort(correct_position):
    result = {'title': "Field Order"}
    if correct_position:
        result['score'] = 'Pass'
    else:
        result['score'] = 'Error'
        result['explanation'] = 'Action Required: Move this column to its correct position'
    return result


def val_column_exist(field_found):
    result = {'title': "Field Exist"}
    if field_found:
        result['score'] = 'Pass'
    else:
        result['score'] = 'Error'
        result['explanation'] = 'Field not found'
    return result


def example_results():
    expl = 'This is an example explanation'
    pass_result = {
        'score': 'Pass',
        'title': 'Pass Example',
        'explanation': expl
    }
    warning_result = {
        'score': 'Warning',
        'title': 'Warning Example',
        'explanation': expl
    }
    error_result = {
        'score': 'Error',
        'title': 'Error Example',
        'explanation': expl
    }
    return [pass_result, warning_result, error_result]


def cells_must_not_be_empty(values) -> dict:
    result = {'title': "Not Empty"}
    rows = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or not value:
            rows.append(get_row(index))
    if not rows:
        result['score'] = 'Pass'
        result['explanation'] = 'All cells are non-blank'
    else:
        result['score'] = 'Error'
        result['explanation'] = 'Action Required. The following rows are blank:'
        result['rows'] = rows
    return result


def get_row(index):
    return index + 2
