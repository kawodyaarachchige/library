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