import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods =10)
df = pd.DataFrame(np.arange(40).reshape((10,4)), index=dates, columns=['A','B','C','D'])

print(df)

print(df['A'])   # get Series from column

print(df.A)

print(df[0:2])   # get rows


print(df['20190103':'20190107'])   # get rows by index

# print(df['20190103'])   # ERROR!
print(df.loc['20190103']) 
