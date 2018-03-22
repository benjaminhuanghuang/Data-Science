import pandas as pd
'''
DataFrame is 2d table
Series is a column in DataFrame
Index is row name
'''
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # Create a series
print(s)
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(d)
d2 = pd.DataFrame(s)   # Create df from series
print(d2)

d.head()  # first 5 row
d.describe()  # 


xls_df = pd.read_excel('data.xls')
csv_df = pd.read_excel('data.csv', encoding='utf-8')
