import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')

x=['강나래', '강태원', '강호림']   
y=[190,187,184]
plt.bar(x, y, color=['r','b','y'], width=0.1)
plt.show()

#-------


plt.bar(df['이름'], df['국어'])
plt.xticks(df['이름'], rotation=45)         #xticks 회전시키기.
plt.show()