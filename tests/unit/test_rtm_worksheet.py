from pathlib import Path
import pytest
from rtm.rtm_worksheet import RTMWorksheet
from rtm.fields import Field, WorksheetColumn, field_classes


def get_path() -> Path:
    return Path(__file__).parent / 'rtm_simple.xlsx'


def test_get_worksheet():
    path = get_path()
    ws_data = RTMWorksheet._get_worksheet(path, worksheet_name='test_worksheet')
    for col in ws_data:
        assert isinstance(col, WorksheetColumn)
    return ws_data


def test_field_list():
    """Ensure that all field classes in the list """
    for field_class in field_classes:
        assert issubclass(field_class, Field)


# @pytest.mark.skip(reason="This is just a test skip")
def test_initialize_fields():
    ws_data = test_get_worksheet()
    field_seq = RTMWorksheet._initialize_fields(
        field_classes=field_classes,
        worksheet_columns=ws_data,
    )
    assert field_seq[0].get_field_name() == 'id'


@pytest.mark.skip(reason="Currently debugging above")
def test_fdr_worksheet():
    path = get_path()
    rtm_worksheet = RTMWorksheet(path)
    assert rtm_worksheet.fields[0].get_field_name() == ['id']


if __name__ == "__main__":
    # test_import_worksheet()
    pass
