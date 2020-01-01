
import pandas as pd

# Load csv
filename = 'data/car_financing.csv'
df = pd.read_csv(filename)

# Load excel
filename = 'data/car_financing.xlsx'
df = pd.read_excel(filename)