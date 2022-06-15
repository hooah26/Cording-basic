# seires : 1차원 배열

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# x=[1,2,3]
# y=[2,4,8]


# plt.plot(x,y)
# plt.title('line graph')
# plt.show()

temp = pd.Series([-20,-10,10,20], index=['jan','feb','mar','apr'])

print(temp)
