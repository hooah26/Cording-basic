import pandas as pd
df= pd.read_excel('출산율.xls', skiprows=2, nrows=3, index_col=0)
print(df)

df.T  #가로세로(행 열) 바꿔 출력