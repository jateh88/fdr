from fdr import WorksheetColumn, FdrWorksheet
from pathlib import Path
# import openpyxl


def test_import_worksheet():
    path = Path(__file__).parent / 'fdr_simple.xlsx'
    ws_name = 'import_worksheet'
    ws_data = FdrWorksheet._import_worksheet(path, ws_name)
    for col in ws_data:
        assert isinstance(col, WorksheetColumn)
    # wb = openpyxl.load_workbook(path)
    # print(f"worksheet names: {wb.sheetnames}")

# if __name__ == "__main__":
#     test_import_worksheet()