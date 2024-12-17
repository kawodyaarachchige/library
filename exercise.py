#craete a 2D numPy array which has dimension  4*5 which contains the numbres 1 to 20 
#perform the following on thsi array add 10 to evey element
#Multify every element by 2
#calculate the squre of each element

import numpy as np

array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(array_1)

array_2 = array_1 + 10
print(array_2)

array_3 = array_1 * 2
print(array_3)

array_4 = array_1 ** 2
print(array_4)