from pathlib import Path
import pytest
from rtm.rtm_worksheet import RTMWorksheet
from rtm.fields import WorksheetColumn, Field, field_classes as fc


def test_initialize_fields(worksheet_columns):
    fields = RTMWorksheet._initialize_fields(
        field_classes=fc, worksheet_columns=worksheet_columns
    )
    for field in fields:
        assert field.field_found


def test_get_worksheet(rtm_path):
    worksheet_columns = RTMWorksheet._get_worksheet_columns(
        path=rtm_path, worksheet_name="test_worksheet"
    )
    for ws_col in worksheet_columns:
        assert isinstance(ws_col, WorksheetColumn)


def test_init_rtm_worksheet(rtm_path):
    rtm_worksheet = RTMWorksheet(rtm_path)
    for field in rtm_worksheet.fields:
        assert isinstance(field, Field)


if __name__ == "__main__":
    # test_import_worksheet()
    pass
