from fdr import WorksheetColumn, field_class_seq
from fdr import ID


def test_field_id():

    # --- Define worksheet columns --------------------------------------------
    ws_col_seq = [
        WorksheetColumn(header="id", values=tuple(range(100))),
        WorksheetColumn(header="device", values=tuple(range(100))),
    ]

    id_field = ID(ws_col_seq)
    assert id_field.indices == [0]
