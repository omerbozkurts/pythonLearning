x,y,z=2,4,6
print(f'x:{x} y:{y} z:{z}')

x,y=y,x
print(f'x:{x} y:{y} z:{z}')

values= 1,2,4
print(values)
print(type(values))

x,y,z=values
print(f'x:{x} y:{y} z:{z}')

values=1,5,4,6,9,3
#x,y,z=values there is an error because there are to many values in values to assignment
x,y,*z=values
print(f'x:{x} y:{y} z:{z}') #we declare like this and z become list
print(z[0])