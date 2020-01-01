import pandas as pd
import numpy as np

# Load excel
filename = 'car_financing.xlsx'
df = pd.read_excel(filename)

# Select top N number of records (default = 5)
df.head()

# Select bottom N number of records (default = 5)
df.tail()

# Check the column data types using the dtypes attribute
# For example, you can wrongly assume the values in one of your columns is 
# a int64 instead of a string. 
df.dtypes

# Use the shape attribute to get the number of rows and columns in your dataframe
df.shape


# The info method gives the column datatypes + number of non-null values
# Notice that we seem to have 408 non-null values for all but the Interest Paid column. 
df.info()


# Select one column
df[['car_type']].head

# Select multip columns
df[['car_type', 'Pricipal Paid']].head

# Select data
df['car_type'][0:10]
