"""Validate a J&J DPS FDR."""
__version__ = '0.1.0'

def main():
    print("It works!")



import pathlib
from bin import excel_data_handler as util

path = pathlib.Path(r"C:\Users\jchukina\JNJ\Roebling - FDR Gen 1 Concepts\Gen 1 Prototype Latest Files")
path /= "20190618 Roebling FDR Gen 1 Prototype.xlsx"
workbook_contents = util.get_dicts_from_excel(path)
ws = workbook_contents['Procedure Based Requirements']

# For each row:
#   determine if it is a procedure step
#   Get first number (the one following the 'P')

orig_number = []
for row in ws:
    orig_number.append(str(row['Req. Number']))

for value in orig_number:
    p_value = util.get_first_integer_sequence(value)
    p_string = 'P' + util.convert_to_string_with_leading_zeroes(p_value, 3) + '-'
h

    print(value, p_value, p_string)
