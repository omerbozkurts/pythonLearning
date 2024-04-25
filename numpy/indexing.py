import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

print(numbers[5])

print(numbers[-1])

print(numbers[0:3])

print(numbers[:3])

print(numbers[3:])

print(numbers[::])

print(numbers[::-1])

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

print(numbers2[0])

print(numbers2[2])

print(numbers2[0,2])

print(numbers2[2,1])

print(numbers2[:,2])

print(numbers2[:,0:2])

print(numbers2[-1,:])

arr1 = np.arange(0,10)

arr2 = arr1

arr2[0]= 18

print(arr1)
print(arr2)

arr1 = np.arange(0,10)
arr2 = arr1.copy()

arr2[0] = 19

print(arr1)
print(arr2)




