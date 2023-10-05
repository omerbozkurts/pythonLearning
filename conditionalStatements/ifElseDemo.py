#q1 get the name, age and education of the driver and check if he/she can get a driver's license
    # must be over eighteen years of age and have a high school or university education

name=str(input("name:"))
age=int(input("age:"))
education=str(input('education:'))

if age>18 and (education=='highschool' or education=='university'):
    print(f"{name} can get a driver's licence ")
else:
    print(f"{name} can't get a driver's licence ")
    
#q2 take the midterm and final grades from the student, calculate the average and write the letter grade equivalent
    # 0-24 => FF
    # 25-44 => FD
    # 45-54 => DD
    # 55-69 => CC
    # 70-84 => BB
    # 85-100 => AA

midterm=int(input('midterm:'))
final=int(input("final"))
average=(midterm*0.4)+(final*0.6)

if average<=24 and average>=0:
    print(f'average is {average} and letter grade is FF')
elif average<=44:
     print(f'average is {average} and letter grade is FD')
elif average<=54:
     print(f'average is {average} and letter grade is DD')
elif average<=69:
     print(f'average is {average} and letter grade is CC')
elif average<=84:
      print(f'average is {average} and letter grade is BB')
elif average<=100:
      print(f'average is {average} and letter grade is AA')
else:
     print('the average is greater than 100 or lower than 0')
if average>50:
     print("student is succeed")
else:
     print('student is failed')


#q3 Calculate the service time of a vehicle with a traffic date based on the following information
    # first service => first year
    # second service => second year
    # third service => third year

import datetime

entryDate=input("what is the vehicle's date of entry into traffic(dd/mm/yyyy):")
entryDate=entryDate.split("/")
entryDate=datetime.datetime(int(entryDate[2]),int(entryDate[1]),int(entryDate[0]))
nowDate=datetime.datetime.now()
substraction=nowDate-entryDate
days=substraction.days

if days<=365:
    print("It's been {} days since the date of its release into traffic.It's first service".format(days))
elif days<=365*2:
    print("It's been {} days since the date of its release into traffic.It's second service".format(days))
elif days<=365*3:
    print("It's been {} days since the date of its release into traffic.It's second service".format(days))
else:
    print('invalid date')