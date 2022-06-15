import numpy as np


a = np.array([[0, 1, 2], [3, 4, 5]])
a[0, 1]  # 첫번째 행의 두번째 열
a[-1, -1]  # 마지막 행의 마지막 열



a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
a[0, :]  # 1번째 행의 모든 열
a[:, 1]  # 모든 행의 2번째 열    [1 5]

print(a[:,1])
print(type(a[:,1]))

print(a)




