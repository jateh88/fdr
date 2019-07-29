from rtm.fields.print_val_results import print_val_header, print_val_result, print_validation_report
import pytest


def test_print_val_header():
    print_val_header("Test Field")


# @pytest.mark.parametrize("single_result", dummy_val_results)
def test_print_val_result(dummy_val_results):
    single_result = dummy_val_results[0]
    print_val_result(single_result)


def test_print_validation_report(dummy_val_results):
    print_validation_report(
        field_name="Test Field",
        all_val_results=dummy_val_results,
    )
