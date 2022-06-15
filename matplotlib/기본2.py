import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')



plt.title('학생성적 그래프')
plt.plot(df['이름'],df['국어'], label='국어')
plt.xlabel('이름')
plt.ylabel('국어')
plt.legend()
plt.show()