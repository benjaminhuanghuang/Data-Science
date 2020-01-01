import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df_abbrevs = pd.read_csv('data/state-abbrevs.csv')
print(df_abbrevs.head())

df_people = pd.read_csv('data/state-population.csv')
print(df_people.head())

# Join
df_merged = df_people.merge(df_abbrevs, left_on="state/region", right_on="abbreviation")
print(df_merged)
