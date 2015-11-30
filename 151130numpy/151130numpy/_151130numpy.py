import numpy as np
from matplotlib import pyplot as plt
list1 = [1,2,3,4,5]
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data*data)
print(data/3)
print(data**2)
print(data.dot(data))
print("----------------------------------")
#원소비교
a=np.array([1,2,3,4])
b=np.array([4,2,2,4])
print(a==b)
print(a>b)
#array비교
c=np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))
print("----------------------------------")
a=np.array([1,1,0,0],dtype=bool)
b=np.array([1,0,1,0],dtype=bool)
print(np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.all([True,True,False]))
print(np.any([True,True,False]))
print("----------------------------------")
a=np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
print("----------------------------------")
a=np.triu(np.ones((3,3)),0)
print(a.T)
print("----------------------------------")
x=np.array([1,2,3,4])
print(np.sum(x))
print(x.sum())

x=np.array([[1,1],[2,2]])
print(x.sum(axis=0)) # columns(first dimension)
print(x.sum(axis=1)) #rows(second dimension)
print("----------------------------------")
x=np.array([1,3,2])
print(x.min())
print(x.argmin())
print("----------------------------------")
print(np.all([True,True,False]))
a=np.zeros((100,100))
print(np.any(a!=0))
print(np.all(a==a))
print("----------------------------------")
x=np.array([1,2,3,1])
y=np.array([[1,2,3],[5,6,1]])
print(x.mean())
print(np.median(x))
print(np.median(y,axis=-1))
x.std()
print("----------------------------------")

data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T

#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()
print(data.mean(axis=0)[1:])
print(data.std(axis=0)[1:])

print(data[data.T[1].argmax(axis=0)][0])
print(data[data.T[2].argmax(axis=0)][0])
print(data[data.T[3].argmax(axis=0)][0])

print("----------------------------------")
data1 = np.arange(6)
data2 = np.array([[0,10,20,30,40,50]]).T



