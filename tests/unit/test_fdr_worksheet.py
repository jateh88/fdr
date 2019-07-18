from fdr import WorksheetColumn, FdrWorksheet
from pathlib import Path
from fdr.fields import field_class_seq, Field

def get_path():
    return Path(__file__).parent / 'fdr_simple.xlsx'

def test_get_worksheet():
    path = get_path()
    ws_name = 'import_worksheet'
    ws_data = FdrWorksheet._get_worksheet(path, ws_name)
    for col in ws_data:
        assert isinstance(col, WorksheetColumn)
    return ws_data

def test_field_list():
    """Ensure that all field clases in the list """
    for field in field_class_seq:
        # field_o = field()
        assert issubclass(field, Field)


def test_initialize_fields():
    ws_data = test_get_worksheet()
    field_seq = FdrWorksheet._initialize_fields(
        field_classes=field_class_seq,
        worksheet=ws_data,
    )
    assert field_seq[0].get_names() == ['id']

def test_fdr_worksheet():
    path = get_path()
    fdr_worksheet = FdrWorksheet(path)
    assert fdr_worksheet.fields[0].get_names() == ['id']



# if __name__ == "__main__":
#     test_import_worksheet()



# TODO: note that I can skip tests, or expect to fail