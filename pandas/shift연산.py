import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(4), index=pd.date_range(
    "2018-1-1", periods=4, freq="M"))
ts
'''
2018-01-31    1.764052
2018-02-28    0.400157
2018-03-31    0.978738
2018-04-30    2.240893
Freq: M, dtype: float64
'''
#shift 연산을 사용하면 인덱스는 그대로 두고 데이터만 이동할 수도 있다.

ts.shift(1)
'''
2018-01-31         NaN
2018-02-28    1.764052
2018-03-31    0.400157
2018-04-30    0.978738
Freq: M, dtype: float64'''