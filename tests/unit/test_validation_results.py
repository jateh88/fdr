from rtm.fields.validation_results import ValidationResult, print_validation_report, print_val_header
import pytest


def test_print_validation_report(example_val_results):
    print_validation_report("Test Field", example_val_results)


def test_print_val_header():
    print_val_header("Test Field")
