import numpy as np

a = np.array([1,2,3])

print (a)



a = np.array([[1,2] , [3,4]])

print (a)



list1 = [1,2,3,4,5]
arr = np.array(list1)
print(arr)


arr2 = np.arange(10,100)
print(arr2)


arr3 = np.zeros((5,5))
print(arr3)


vector = np.linspace(0,20,5)
print(vector)


x=[1,2,3]
a=np.asarray(x)
print(a)



zarr= np.zeros(8)
arr3d = zarr.reshape((2,2,2))
print(arr3d)



zarr= np.zeros(8)
arr3d = zarr.reshape((2,2,2))
arr=arr3d.ravel()
print(arr)



arr = np.arange(2,20)
element = arr[6]
print(element)



arr = np.arange(20)
arr_slice = slice(1,10,2)
element = arr[6]
print(arr[arr_slice])


arr=np.arange(20)
print(arr[2:])

print(arr[:15])


a=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[0:2,0:2])


print(a.shape)
print(a.ndim)
print(a.itemsize)

import numpy as np
x1= np.empty([3,2])
print(x1)


x=np.zeros(5)
print(x)


###############################

##SERIES

import pandas as pd

series = pd.Series()

print(series)


arr=np.array([10,20,30,40,50])
series=pd.Series(arr)
print(series)



data = {'a':10,'b':20,'c':30}
series=pd.Series(data)
print(series)


s = pd.Series([10,20,30,40,50])
print(s[1:4])


listx = [10,20,30,40]
table = pandas.DataFrame(listx)
print(table)





















