import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False   #이렇게 해야 - 기호가 음수의 의미로 쓰임

df= pd.read_excel('score.xlsx')

x=[1,2,3]
y=[2,4,8]  #x와 y축의 데이터를 리스트로 직접 넣을 수도 있음.
plt.plot(x,y) 

# plot: 선.   bar넣으면 막대기. pie하면 원.

plt.bar(df['이름'], df['키'])     #x축에 이름 값 정렬, y축에 키 값 정렬
plt.title('라인 그래프- Line graph')
plt.show()

plt.xlabel('이름', loc='right', color='red')
plt.ylabel('키', loc='top', color='#ff0000')

plt.yticks([150,200,300,350])   #yticks 구분
plt.xticks([1,2,3])
plt.title('꺾은선그래프')
plt.plot(x,y,label='범례데이터')          #여기서의 라벨은 plot-선의 라벨.
plt.legend()  #라벨 보이려면.
plt.show()