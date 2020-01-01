import pandas as pd
carLoans = [[1, 34689.96, 687.23, 202.93, 484.3, 34205.66, 60, 0.0702,'Toyota Sienna'],
           [2, 34205.66, 687.23, 200.1, 487.13, 33718.53, 60, 0.0702,'Toyota Sienna'],
           [3, 33718.53, 687.23, 197.25, 489.98, 33228.55, 60, 0.0702,'Toyota Sienna'],
           [4, 33228.55, 687.23, 194.38, 492.85, 32735.7, 60, 0.0702,'Toyota Sienna'],
           [5, 32735.7, 687.23, 191.5, 495.73, 32239.97, 60, 0.0702,'Toyota Sienna']]

colNames = ['Month',
            'Starting Balance',
            'Repayment',
            'Interest Paid',
            'Principal Paid',
            'New Balance',
            'term',
            'interest_rate',
            'car_type']
df = pd.DataFrame(data=carLoans, columns=colNames)

# Save to csv
df.to_csv(path_or_buf='data/temp.csv', index=False)

# Save to excel
df.to_excel(excel_writer='data/temp.xlsx', index=False)
