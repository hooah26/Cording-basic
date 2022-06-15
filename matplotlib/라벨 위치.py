import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


x=[1,2,3]
y=[2,4,8]
plt.plot(x,y,label='범례')
# plt.legend(loc='upper right')
plt.legend(loc=(0.7,0.8))
plt.show()