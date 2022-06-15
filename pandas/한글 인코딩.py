import pandas as pd
df= pd.read_csv('월별.csv', encoding='euc-kr')   #euc-kr 한국에서만 적용
print(df)

#csv는 인코딩 주의