def cube():
    result=[]
    for i in range(5):
        result.append(i)
    return result

iterator=iter(cube())

print(next(iterator))
print(next(iterator))


def cube2():
    for i in range(5):
        yield i**3

generator=cube2()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))


generator=cube2()

for i in generator:
    print(i)


listB=(i**3 for i in range(5))
print(listB)

iterator=iter(listB)
print(next(iterator))

for i in listB:
    print(i)