import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
cvalues= [20,34,45.1]
#conver values  into 1-d array
c=np.array(cvalues)
print(c)
#celsius to fahrenheit
print(c*9/5 + 32)
array1=np.array([[21,22,23,45],[34,45,78,34]],dtype=float)
#Myarray=numpy.array([1,2,3,4])
#print array
print(array1)
print(array1.shape)
print(array1.itemsize)
print(array1.ndim)


