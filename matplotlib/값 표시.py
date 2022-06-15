import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')

x=[10,20,30]
y=[2,4,8]

plt.plot(x,y, marker='o')
plt.yticks([2,4,6,8,10])
for idx,txt in enumerate(y):         #x든 y든  idx는 개수라서 같음. 근데 txt로 y값을 쓰고 있음. y값을 적는 거지.
    plt.text(x[idx],y[idx]+0.3, txt, ha='center')

plt.grid(axis='both') #격자무늬
plt.show()