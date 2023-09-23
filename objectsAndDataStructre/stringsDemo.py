website='http://www.github.com/omerbozkurts'
text="lorem ipsum dolar sit amet, consectetur adipiscing elit"

#q1: how many character in text string ?

lengthTS=len(text)
print(lengthTS)

#q2: choose the www character in the website string

print(f"the choosen characters are: {website[7:10]}")               #a1
print("the choosen characters are: {w}".format(w=website[7:10]))    #a2

#q3: choose first 15 and last 15 character in the text

answer3=text[:15]+text[-15:]
print(answer3)

#q4: print reverse the text

print(text[::-1])

#q5: write 'abc' 3 times

print('abc '*3)     #a1
a='abc '*3
print(a)            #a2