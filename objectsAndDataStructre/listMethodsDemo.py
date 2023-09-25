names=['Ali','Yagmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#q1 add "Cenk" end of the names list

names.append('Cenk')
print(names)

#q2 add "Sena" top of the names list

names.insert(0,'Sena')
print(names)

#q3 delete the "Deniz" in the names list

names.remove('Deniz')
print(names)

#q4 is "Ali" a component of the names list

isThere= 'Ali' in names
print(isThere)

#q5 reverse the names list components

names.reverse()
print(names)

#q6 sort the names list alpabetically

names.sort()
print(names)

#q7 sort the years list

years.sort()
print(years)

#q8 make str="Chevrolet,Dacia" a list

str='Chevrolet,Dacia'
str=str.split(',')
strList=[str[0],str[1]]
print(strList)

#q9 what is the minimum and maximum value of years list

minYears=min(years)
maxYears=max(years)
print("min value: {} max value: {}".format(minYears,maxYears))

#q10 how many '1998' component in the years list

counter1998=years.count(1998)
print(counter1998)

#q11 remove whole components in the years list

years.clear()
print(years)

#q12 make a list with 3 company names that given by user

cmp1=input('first company:')
cmp2=input("second company:")
cmp3=input('third company:')

companies=[cmp1,cmp2,cmp3]
print(companies)