name="Ali"
surname='Yilmaz'
age=41

print('name: {} surname: {} age: {}'.format(name,surname,age))          #curly bracket is make possible to give the variable in the string
print("surname: {1} age: {2} name: {0}".format(name,surname,age))       #write index in the curly bracket and the order is change
print('surname: {s} age: {a} name: {n}'.format(n=name,s=surname,a=age)) #also you can give a name to variables and you can use it for ordering


divide=200/700

print(divide)
print("result is: {d:1.3}".format(d=divide))                            #you can choose how many number shown after the float point

print(f'name: {name} surname: {surname} age: {age}')                    #also using the f letter you can give the variables in the string