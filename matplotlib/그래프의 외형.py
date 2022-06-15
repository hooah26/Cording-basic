
import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


x=[1,2,3]
y=[2,4,8]
plt.figure(figsize=(10,5), facecolor='yellow')   #그래프 전체의 외형, 가로세로 인치.  dpi는 해상도. 해상도가 커지면 .. 화질이 좋아지고 이미지가 커진다 ? facecolor는 배경색
plt.plot(df['이름'],df['국어'])
plt.plot(df['이름'],df['영어'])
plt.plot(df['이름'],df['수학'])
plt.show()