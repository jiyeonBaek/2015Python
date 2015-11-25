﻿import numpy as np
from matplotlib import pyplot as plt

data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print("--------------------------------------------")
np.eye((3))
print(np.array([1,2,3,4]))
print(np.diag(np.array([1,2,3,4])))
print(data.T)
print("--------------------------------------------")
print(np.arange(10))
print(np.arange(10,1,-1))
print(np.arange(35).reshape(5,7))
print("--------------------------------------------")
print(np.linspace(1.,4.,6))
print(np.linspace(1.,4.,6, endpoint=False))
print("-------------------------------------------")

data = np.random.rand(4)
print(data)
data = np.random.randn(16).reshape(4,4)
print(data)
print("-------------------------------------------")
#data = np.loadtxt('data.txt')
#print(data)
#year, hares, lynxes, carrots = data.T
#print(year)
print("-------------------------------------------")
data = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(data[0]) # 첫번째행
print(data[-1])
print(data[0:2]) #처음부터 2개
print(data[:2])
print(data[::-1])
print(data[2,1])
print(data[2][1])
print(data[1:4:2])
print(data[1:4:2,::3])
print("-------------------------------------------")
x=np.arange(10,1,-1)
print(x[np.array([3,3,1,8])])
print(x[np.array([[1,1],[2,3]])])
print("-------------------------------------------")
y=np.arange(35).reshape(5,7)
print(y[np.array([0,2,4])])
b=y>20
print(y[b])
print("-------------------------------------------")
data = np.arange(36).reshape(6,6)
mask = np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(data)
print(data[mask,2])
mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data[mask1,mask2])

mask3 = np.array([0,2,5])
print(data[3:,mask3])