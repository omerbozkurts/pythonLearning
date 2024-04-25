import numpy as np

pyList = [1,2,3,4,5,6,7,8,9]

npArray = np.array([1,2,3,4,5,6,7,8,9])

print(type(pyList))
print(type(npArray))


pyMulti = [[1,2,3],[4,5,6],[7,8,9]]
npMulti = npArray.reshape(3,3)

print(pyMulti)
print(npMulti)

print(npArray.ndim)
print(npMulti.ndim)

print(npArray.shape)
print(npMulti.shape)