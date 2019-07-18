from fdr import WorksheetColumn
from fdr import FdrWorksheet
from pathlib import Path


def test_import_worksheet():
    path = str(Path('fdr_simple.xlsx').resolve())
    ws_name = 'import_worksheet'
    ws_data = FdrWorksheet._import_worksheet(path, ws_name)
    for col in ws_data:
        assert isinstance(col, WorksheetColumn)


# def test_field_id():
#
#
#
#     # --- Define worksheet columns --------------------------------------------
#     ws_col_seq = [
#         WorksheetColumn(header="id", values=tuple(range(100))),
#         WorksheetColumn(header="device", values=tuple(range(100))),
#     ]
#
#     id_field = ID(ws_col_seq)
#     assert id_field.indices == [0]

test_import_worksheet()