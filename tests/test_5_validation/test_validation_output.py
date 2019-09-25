# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
import pytest

# --- Intra-Package Imports ---------------------------------------------------
import rtm.validate.validator_output as vo


def test_validation_result(capsys):

    # --- Create sample validation output -------------------------------------
    title = 'You fAIL'
    score = 'Error'
    explanation = 'here are the rows that failed: '
    indices = list(range(5))
    validation_result = vo.ValidationResult(score, title, explanation, indices)

    # --- Capture result ------------------------------------------------------
    validation_result.print()
    captured = capsys.readouterr()

    # --- Compare to expected
    partial_expected_capture = '\tError\tYOU FAIL'.expandtabs(8)
    assert validation_result.pretty_rows == '2-6'
    assert partial_expected_capture in captured.out


def test_output_header(capsys):
    output_header = vo.OutputHeader("Hi")
    output_header.print()
    captured = capsys.readouterr()
    expected_capture = '\n++++++++\n+  Hi  +\n++++++++\n\n'
    assert captured.out == expected_capture
