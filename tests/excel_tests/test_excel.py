import openpyxl
from pathlib import Path


def test_integers_from_excel():

    path = Path(__file__).parent / "test.xlsx"
    wb = openpyxl.load_workbook(filename=path, read_only=True)
    ws = wb["integer"]
    start_row = 1
    end_row = ws.max_row
    for row in range(start_row, end_row + 1):
        assert_type = ws.cell(row, 1).value
        value = ws.cell(row, 2).value
        try:
            value = int(value)
        except (TypeError, ValueError):
            # Value stays as-is
            pass
        if assert_type == "pass":
            assert isinstance(value, int)
        elif assert_type == "fail":
            assert not isinstance(value, int)
        else:
            raise ValueError("Assert Type must be 'pass' or 'fail'.")
