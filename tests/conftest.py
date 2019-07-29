import pytest
from pathlib import Path
from rtm.fields import WorksheetColumn
from typing import List
from rtm.fields.validation import example_results


@pytest.fixture(scope="session")
def worksheet_columns() -> List[WorksheetColumn]:
    headers = [
        "ID",
        "Devices",
        "Requirement Statement",
        "Requirement Rationale",
        "Cascade Level",
        "Verification or Validation Strategy",
        "Verification or Validation Results",
        "Design Output Feature (with CTQ ID #)",
        "CTQ? Yes, No, N/A",
    ]
    return [WorksheetColumn(header, [1, 2, 3]) for header in headers]


@pytest.fixture(scope="session")
def rtm_path() -> Path:
    return Path(__file__).parent / "test_rtm.xlsx"


@pytest.fixture(scope="session")
def dummy_val_results() -> List[dict]:
    return example_results()
