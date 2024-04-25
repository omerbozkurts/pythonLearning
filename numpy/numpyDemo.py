# 1- (10,15,30,45,60) create a numpy array with these values
# 2- (5-15) create a numpy array between this values
# 3- (50-100) create a numpy array between this values that increments 5
# 4- create a ten element array that consisting of zeros 
# 5- create a ten element array that consisting of ones
# 6- (0-100) create a array that equally spaced between these values
# 7- (10-30) create random 5 number between these values
# 8- [-1 and 1] create 10 number between these values
# 9- Generate a random matrix of size (3x5) between (10-50)
# 10-Calculate the sums of the row and column numbers of the generated matrix
# 11- what is the maximum, minimum and average of the produced matrix
# 12- what is the largest index of the produced matrix
# 13- Select the first 3 elements of the array containing numbers between (10-20) 
# 14- write the elements of the generated array in reverse order
# 15- select the first row of the generated matrix
# 16- what is the element in the 2nd row and 3rd column of the generated matrix
# 17- select the first element in all rows of the generated matrix
# 18- square each element of the generated mantissa
# 19- which of the generated matrix elements is a positive even number
# make the range between (-50,+50)

import numpy as np

array = np.array([10,15,30,45,60])

print(array)

array = np.arange(5,15)

print(array)

array = np.arange(50,100,5)

print(array)

array = np.zeros(10)

print(array)

array = np.ones(10)

print(array)

array = np.linspace(0,100,5)

print(array)

array = np.random.randint(10,30,5)

print(array)

array = np.random.randn(10)

print(array)

array = np.random.randint(10,50,15).reshape(3,5)

print(array)

print(array.sum(axis=1))
print(array.sum(axis=0))

max = array.max()
min = array.min()
avg = array.mean()

print(max,min,avg)


array2 = np.arange(10,20)

print(array2[:3])

print(array2[::-1])

print(array[0])

print(array[1,3])

print(array[:,0])

print(np.sqrt(array))

array = np.random.randint(-50,50,20)

print(array)

evens = array[array%2==0]

print(evens[evens>0])