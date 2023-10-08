txt='merhaba'

for letter in txt:
    print(letter)

print('\n')

for letter in txt:
    if letter=='h':
        break
    print(letter)

print('\n')

for letter in txt:
    if letter=='h':
        continue
    print(letter)

print('\n')

num=0

while num<10:
    print(num)
    num+=1

print('\n')

num=0

while num<10:
    if num==5:
        num+=1
        continue
    print(num)
    num+=1

print('\n')

num=0

while num<10:
    if num==5:
        break
    print(num)
    num+=1