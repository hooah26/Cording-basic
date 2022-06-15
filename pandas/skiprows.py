import pandas as pd



df = pd.read_excel('pandas_code.xlsx', skiprows=[500], nrows=10)
df = pd.read_excel('pandas_code.xlsx', skiprows=[i for i in range(1,500)], nrows=10)

print(df)
