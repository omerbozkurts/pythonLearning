import numpy as np

npArray = np.array([1,3,5,9])

print(npArray)

npArray = np.arange(1,10)

print(npArray)

npArray = np.arange(10,100,3)

print(npArray)

npArray = np.zeros(10)

print(npArray)

npArray = np.ones(10)

print(npArray)

npArray = np.linspace(0,100,5)

print(npArray)

npArray = np.random.randint(0,20)

print(npArray)

npArray = np.random.rand(5)

print(npArray)

npArray = np.arange(50)

npArray = npArray.reshape(5,10)

print(npArray)

print(npArray.sum(axis=1))


npArray = np.random.randint(0,100,10)

print(npArray)
print(npArray.max())
print(npArray.min())
print(npArray.mean())
print(npArray.argmax())
