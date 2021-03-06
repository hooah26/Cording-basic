import numpy as np

#배열 인덱싱
'''
팬시 인덱싱(fancy indexing) = 배열 인덱싱(array indexing). 
인덱싱이라는 이름이 붙었지만 사실은 데이터베이스의 질의(Query) 기능을 수행한다. 
배열 인덱싱에서는 대괄호(Bracket, [])안의 인덱스 정보로 숫자나 슬라이스가 아니라 위치 정보를 나타내는 또 다른 ndarray 배열을 받을 수 있다. 
여기에서는 이 배열을 편의상 인덱스 배열이라고 부르겠다. 

배열 인덱싱의 방식에은 불리언(Boolean) 배열 방식과 정수 배열 방식 두가지가 있다.

'''

#불리언 배열 인덱싱
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True,
               False, True, False, True, False])
print(a[idx])

print(a%2==0)   #각 데이터마다 불린값
print(type(a%2==0))   #array 객체

print(a[a%2==0])    #불린값을 넣어서 뽑아넨다.



# 정수 배열 인덱싱
a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
a[idx]   #array([11, 33, 55, 77, 99])


a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
a[idx]   #array([11, 11, 11, 11, 11, 11, 22, 22, 22, 22, 22, 33, 33, 33, 33, 33])




#다차원 배열의 배열 인덱싱

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[:, [True, False, False, True]]    #모든 행에 대해서 각각의 열에 해당 조건을 넣음 # ([[ 1,  4],   [ 5,  8],  [ 9, 12]])
a[[2, 0, 1], :]   #[[ 9, 10, 11, 12],   [ 1,  2,  3,  4],   [ 5,  6,  7,  8]]
