import openpyxl


def test_integers_from_excel():
    wb = openpyxl.load_workbook('test.xlsx')
    ws = wb['integer']
    print(ws.max_row)
    # for row in range(ws.max_row):
        # row_contents = dict()
        # key = ws.cell(1, col).value
        # value = ws.cell(row, col).value
        # row_contents[key] = value
        # worksheet_contents.append(row_contents)

test_integers_from_excel()
