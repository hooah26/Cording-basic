import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


x=[1,2,3]
y=[2,4,8]
plt.plot(x,y)

plt.savefig('graph.png')   #여기서 dpi 지정할 수 있음.


# plt.show () 로 표시된 이미지를 닫으면 이미지가 닫히고 메모리에서 해제된다.
#show 를 호출하기 전에 savefig 및 savetxt 를 호출해야한다.
