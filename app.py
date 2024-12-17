import numpy as np

a = np.array([1, 2, 3])
print("Type of a :",type(a))  

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

print("Addition: ",array_1 + array_2)# addition
print("Multiplication :",array_1 * array_2)# multiplication
print("Subtraction :",array_1 - array_2)# subtraction
print("Division :",array_1 / array_2)# division
print("Square root :",np.sqrt(array_1))# square root
print("Sum :",np.sum(array_1))
print("Mean :",np.mean(array_1))# mean

#Maxium and Minimum
print("Maximum:",np.max(array_1))
print("Minimum:",np.min(array_1))
print("Maximum:",np.max(array_2))
print("Minimum:",np.min(array_2))

#Multidimensional array
#2D Array
array_3 = np.array([[6,7,8],[9,10,11]])
print("Multidimensional array",array_3)
print("Size of array :",array_3.size)
print("Row and column :",array_3.shape)

#3D Array
array_4 = np.array([[[4,5,6],[1,2,3]],[[7,8,9],[10,11,12]]])
print(array_4)
print(array_4.shape)
print("---------------")
#4D Array
array_5 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],[[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]])
print(array_5)
print(array_5.shape)

#dtype
#data type of elements stored in array
print("dtype of array_4 :",array_4.dtype)

#ndim
#number of dimensions of array
print("ndim of array_4 :",array_5.ndim)

#index
print(array_3[1,2])
print(array_4[0,1,2])