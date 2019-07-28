import pytest
from pathlib import Path
from rtm.fields import WorksheetColumn


@pytest.fixture(scope="session")
def worksheet_columns():
    headers = "ID Devices".split()
    return [WorksheetColumn(header, [1, 2, 3]) for header in headers]


@pytest.fixture(scope="session")
def rtm_path() -> Path:
    return Path(__file__).parent / "test_rtm.xlsx"
