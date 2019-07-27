from pathlib import Path
import pytest
from rtm.rtm_worksheet import RTMWorksheet
from rtm.fields import WorksheetColumn, field_classes


def get_path() -> Path:
    return Path(__file__).parent / "rtm_simple.xlsx"



def test_initialize_fields(worksheet_columns):
    fields = RTMWorksheet._initialize_fields(
        field_classes=field_classes,
        worksheet_columns=worksheet_columns,
    )
    assert fields[0].get_field_name() == "id"


@pytest.mark.skip(reason="Currently debugging another test")
def test_get_worksheet():
    path = get_path()
    ws_data = RTMWorksheet._get_worksheet_columns(path, worksheet_name="test_worksheet")
    for col in ws_data:
        assert isinstance(col, WorksheetColumn)
    return ws_data


@pytest.mark.skip(reason="Currently debugging above")
def test_fdr_worksheet():
    path = get_path()
    rtm_worksheet = RTMWorksheet(path)
    assert rtm_worksheet.fields[0].get_field_name() == ["id"]


if __name__ == "__main__":
    # test_import_worksheet()
    pass
