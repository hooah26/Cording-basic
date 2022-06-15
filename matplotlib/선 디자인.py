
import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


x=[1,2,3]
y=[2,4,8]
plt.plot(df['이름'],df['국어'],linewidth=2, marker='o', markersize=10, markerfacecolor='red', markeredgecolor='green' , linestyle='--' , label='국어')
plt.plot(df['이름'],df['영어'],linewidth=2, marker='o', ms=10, mfc='red', mec='green' , ls='--' , label='영어', alpha=0.4)
plt.plot(df['이름'],df['수학'], 'ro--',  linewidth=2,  ms=10,  mec='green' , label='수학')  #축약도 가능


plt.legend()
plt.show()