"""This module defines functions related to the pandas dataframe extracted from
the procedure-based requirements excel worksheet."""

# --- Standard Library Imports ------------------------------------------------
from difflib import SequenceMatcher

# --- Third Party Imports -----------------------------------------------------
# None

# --- Intra-Package Imports ---------------------------------------------------
# None


def map_expected_to_actual(expected_strings: set, actual_strings: set):
    """
    Used for mapping field names to their exact or best matches in pandas dataframe.
    :param expected_strings: strings for whom we seek the best match
    :param actual_strings: available strings
    :return: dict[expected_string] = actual_string
    """
    result = {}

    # --- Get exact matches ---------------------------------------------------
    for string in expected_strings & actual_strings:
        result[string] = string
    remaining_expected = list(expected_strings - actual_strings)
    remaining_actual = list(actual_strings - expected_strings)

    # --- Order expected strings by best match --------------------------------
    def sort_by_match_ratio(input_string):
        return find_best_match(
            string=input_string,
            strings=list(remaining_expected),
            return_ratio=True,
        )
    remaining_expected.sort(key=sort_by_match_ratio)

    # --- Find best match for each remaining string ---------------------------
    for string in remaining_expected:
        best_actual = find_best_match(string, remaining_actual)
        result[string] = best_actual
        remaining_actual.remove(best_actual)

    # --- Return result -------------------------------------------------------
    return result


def find_best_match(string: str, strings: list, return_ratio=False):
    """Return the best match to a given string."""
    ratios = [
        SequenceMatcher(None, string, orig_string).ratio()
        for orig_string in strings
    ]
    max_ratio = max(ratios)
    if return_ratio:
        return max_ratio
    else:
        return ratios.index(max_ratio)
