
import pandas as pd

# Load csv
filename = 'data/car_financing.csv'
df = pd.read_csv(filename)

filename = 'data/state-abbrevs.csv'
df = pd.read_csv(filename, sep=',', header=None, names=['column1','column2'])

# Load excel
filename = 'data/car_financing.xlsx'
df = pd.read_excel(filename)

# Load mysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='test')
data = pd.read_sql('select * from mytable', con=conn)