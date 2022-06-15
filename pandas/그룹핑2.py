import pandas as pd
import numpy as np

np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
df2
'''  
key1 key2  data1  data2
0    A  one      1     10
1    A  two      2     20
2    B  one      3     30
3    B  two      4     40
4    A  one      5     50'''

groups = df2.groupby(df2.key1)    #df2를 df2의 key1열의 값으로 구분한다
groups #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000275865BB700>

groups.groups   #{'A': [0, 1, 4], 'B': [2, 3]}.   리스트 안에 인덱스가 들어갔네.
groups.sum()
'''
      data1  data2
key1
A         8     80
B         7     70'''



a= df2.data1.groupby([df2.key1, df2.key2]).sum()     #df2의 data1열에서 df2의 key1열로 1차분류 key2로 2차분류해서 data1의 합 구함

'''
key1  key2
A     one     6
      two     2
B     one     3
      two     4'''


