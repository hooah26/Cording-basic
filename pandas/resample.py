import pandas as pd
import numpy as np


'''
resample- 시간 간격을 재조정하는 리샘플링(resampling).
시간 구간이 작아지면 데이터 양이 증가한다고 해서 업-샘플링(up-sampling)
시간 구간이 커지면 데이터 양이 감소한다고 해서 다운-샘플링(down-sampling).'''

ts = pd.Series(np.random.randn(100), index=pd.date_range(
    "2018-1-1", periods=100, freq="D"))
ts.tail(5)
'''
2018-04-06    0.401989
2018-04-07    1.883151
2018-04-08   -1.347759
2018-04-09   -1.270485
2018-04-10    0.969397
Freq: D, dtype: float64'''


'''
다운-샘플링의 경우에는 원래의 데이터가 그룹으로 묶이기 때문에 
그룹바이(groupby)때와 같이 그룹 연산을 해서 대표값을 구해야 한다.'''
ts.resample('W').mean()
'''
2018-03-18   -0.450379
2018-03-25    0.601892
2018-04-01    0.334893
2018-04-08    0.509605
2018-04-15   -0.150544
Freq: W-SUN, dtype: float64'''



#ohlc 메서드는 구간의 시고저종(open, high, low, close)값을 구한다.



'''업-샘플링의 경우에는 실제로 존재하지 않는 데이터를 만들어야 한다. 
앞에서 나온 데이터를 뒤에서 그대로 쓰는 forward filling 방식/ 뒤에서 나올 데이터를 앞에서 미리 쓰는 backward filling 방식. 
각각 ffill, bfill 메서드를 이용한다.'''