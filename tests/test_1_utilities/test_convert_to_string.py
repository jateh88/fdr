
def convert_to_string(value):
    try:
        return str(value)
    except KeyError:
        return ''


def test_convert_to_string():
    inputs = [None, 1, 'hello', '']
    expected_output = ['', '1', 'hello', '']
    actual_output = []

    for val in inputs:
        actual_output.append(convert_to_string(val))

    assert actual_output == expected_output
