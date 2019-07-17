import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def get_new_path_from_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = Path(filedialog.askopenfilename())
    return file_path


def get_excel_worksheet_data(path, worksheet_name):
    # TODO add a check to see if this is a valid path.
    #   Add a try
    wb = openpyxl.load_workbook(path)
    if worksheet_name not in wb.worksheets:
        raise ValueError(f"'{worksheet_name} worksheet not found.")
        # TODO replace valueerror with custom validation error
        # TODO: add extra functionality. If exact worksheet name is not found,
        #   use the most similar one and inform user of this.
    ws = wb[worksheet_name]
    ws_data = dict()
    start_column_num = 1
    for col in range(start_column_num, ws.max_column + 1):
        header_name = ws.cell(1, col).value
        values = []
        for row in range(2, ws.max_row + 1):
            values.append(ws.cell(row, col).value)
        ws_data[col] = {'header_name': header_name, 'values': tuple(values)}
    ws_data['start_column_num'] = start_column_num
    return ws_data
