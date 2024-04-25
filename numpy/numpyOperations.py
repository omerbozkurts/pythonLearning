import numpy as np

numbers1 = np.random.randint(10,100,6)

numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

print(numbers1 + numbers2)

print(numbers1 + 10)

print(numbers1 * numbers2)

print(np.sin(numbers1))

print(np.sqrt(numbers1))

print(np.log(numbers1))

mNumbers1 = numbers1.reshape(2,3)
mNumbers2 = numbers2.reshape(2,3)

print(mNumbers1)
print(mNumbers2)


print(np.vstack((numbers1,numbers2)))

print(np.hstack((numbers1,numbers2)))

print(numbers1>=5)

print(numbers1%2==0)

print(numbers1[numbers1%2==0])

