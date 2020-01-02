import pandas as pd
import numpy as np

# Create series with default index
s = pd.Series([4, 5, 6, 9])
print(s)
print(s.values)
print(s.index)   # RangeIndex [0, 4)


# Create series with index
s = pd.Series([4, 5.9, 6, 9], index=['a','b','c','a'])
print(s)
print(s['a'])         # get 3 values
print(s[['a', 'b']])    # multiple index
print('e' in s)

# Create series from dict, keys will be used as index
dict1 = {'a':1, 'b':2, 'c':3}
s = pd.Series(dict1)
print(s)
