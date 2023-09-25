numbers=[0,1,41,4,23,5,29,39,32,23,96,75]
letters=['f','b','d','j','u','g','s']

minNumber=min(numbers)
maxNumber=max(numbers)
print(f'min number: {minNumber} max number: {maxNumber}')

minLetter=min(letters)
maxLetter=max(letters)
print(f'min letter: {minLetter} max letter: {maxLetter}')

print(numbers[3])
print(numbers[3:9])

print(letters[1])
print(letters[:4])

numbers[1]=77
print(numbers)

numbers.append(13)
print(numbers)
numbers.insert(2,53)
print(numbers)
letters.append('h')
print(letters)
letters.insert(3,"o")

numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)
letters.pop()
print(letters)

numbers.remove(29)
print(numbers)
letters.remove('j')
print(letters)

numbers.sort()
print(numbers)
letters.sort()
print(letters)

numbers.reverse()
print(numbers)

print(len(letters))
print(numbers.count(23))
