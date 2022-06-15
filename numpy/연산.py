import numpy as np

x = np.array([1, 2, 3, 4, 10])

np.sum(x)  #10
x.min() #1
x.max() #10
x.argmin()  # 최솟값의 위치

x.mean()  #4
np.median(x)  #3 


'''
연산의 대상이 2차원 이상인 경우에는 어느 차원으로 계산을 할 지를 axis 인수를 사용하여 지시한다. 
axis=0인 경우는 열 연산, axis=1인 경우는 행 연산이다. 
디폴트 값은 axis=0이다. 
axis 인수는 대부분의 차원 축소 명령에 적용할 수 있다.
'''
x = np.array([[1, 1], [2, 2]])
x.sum(axis=0)   # 열 합계    array([3, 3])
x.sum(axis=1)   # 행 합계   array([2, 4])