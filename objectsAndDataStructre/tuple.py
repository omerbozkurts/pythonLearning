listA=['ahmet','ayse','fatma']
tupleA='zeynep','mehmet','ali'

print(listA)
print(tupleA)

print(listA[1])
print(tupleA[1])

listA=['hasan','merve']
tupleA= 'elif','ibrahim'

print(listA)
print(tupleA)

listA[0]='mustafa'
# tupleA[0]='lale' we can't assgiment to tuple because tuple does not support item assignment

tupleA='zeynep','hasan','merve','elif','ibrahim','zeynep','mehmet','ali','zeynep'
print(tupleA.count('zeynep'))
print(len(tupleA))
print(tupleA.index('hasan'))