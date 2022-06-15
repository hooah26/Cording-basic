import numpy as np

c = np.array([[0, 1, 2,3], [3, 4, 5,2], [6,7,8,4]])
print(c.ndim)   #2차원
print(c.shape)   # 3x4


d = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14],
               [15, 16, 17, 18],
               [19, 20, 21, 22]]]) 

print(d.ndim)    #3차원.  # 2 x 3 x 4 array    깊이 2, 행3, 열4 .. 깊이 개념까지 있으니 3차원
print(d.shape)   #(2,3,4)