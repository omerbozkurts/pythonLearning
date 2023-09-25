#q1 make a list that contain 'Bmw' , 'Mercedes' , 'Opel' , 'Mazda'

cars=['Bmw','Mercedes','Opel','Mazda']

#q2 how many componenet list have

count=len(cars)
print(count)

#q3 what is the first and last componenet of list

firstCmp=cars[0]
lastCmp=cars[-1] #lastCmp=cars[count-1]
print(f'first cmp is: {firstCmp} last cmp is: {lastCmp}')

#q3 change mazda to toyota 

mazdaIndex=cars.index('Mazda')
cars[mazdaIndex]='Toyota'
print(cars)

#q4 is 'mercedes' a component of list

isCmp='Mercedes' in cars
print(isCmp)

#q5 add 'Audi' and 'Nissan' to list

cars2=['Audi','Nissan']
cars+=cars2
print(cars)

#q6 delete the last component to the list

del cars[-1]
print(cars)

#q7 print list as reverse

print(cars[::-1])

#q8 make another list with student info list

studentA=['Ali','Yilmaz',2005,[70,60,70]]
studentB=['Ahmet','Yildirim',2003,[80,75,70]]
studentC=['Zeynep','Celik',2004,[80,80,75]]
students=[studentA,studentB,studentC]
print(students)
print(students[1][3][1])