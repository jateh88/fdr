import pandas as pd
import pathlib


path = pathlib.Path(__file__).parent.parent/'test_rtm.xlsx'
sheet_name = 'pandas_experiment'
header_row = 1

# pdre = pd.read_excel
df = pd.read_excel(
    io=path,
    sheet_name=sheet_name,
    header=header_row-1,
    dtype=object,
)

print(df)
print()
print('HEADERS\n', df[['bye']])
bye = df['bye']
print('\n', bye)
for row in bye.tolist():
    print(row)
print(list(bye))
print(list(df['bye.1']))





# import pandas as pd
#
# d = {'one' : pd.Series([1., 2., 3.],     index=['a', 'b', 'c']),
#      'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
#
# df = pd.DataFrame(d)
#
# print("Starting with this dataframe\n", df)
#
# print("The first column is a", type(df['one']), "\nconsisting of\n", df['one'])
#
# dfToList = df['one'].tolist()
#
# dfList = list(df['one'])
#
# dfValues = df['one'].values
#
# print("dfToList is", dfToList, "and it's a", type(dfToList))
# print("dfList is  ", dfList,   "and it's a", type(dfList))
# print("dfValues is", dfValues, "and it's a", type(dfValues))
