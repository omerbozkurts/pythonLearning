import pandas as pd
import numpy as np

numbers = [20,30,40,50]
letters = ['a','b','c','d','f']
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40}
randomNumbers = np.random.randint(10,100,6)

pandasSeries = pd.Series(numbers)

print(pandasSeries)

pandasSeries = pd.Series(letters)

print(pandasSeries)

pandasSeries = pd.Series(scalar)

print(pandasSeries)

pandasSeries = pd.Series(5,[0,1,2,3])

print(pandasSeries)

pandasSeries = pd.Series(numbers,['a','b','c','d'])

print(pandasSeries)

pandasSeries = pd.Series(dict)

print(pandasSeries)

pandasSeries = pd.Series(randomNumbers)

print(pandasSeries)