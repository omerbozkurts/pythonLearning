text='Lorem ipsum dolar sit amet. Consectetur adipiscing elit'

print(text)

text=text.upper()       #upper case for whole text
print(text)

text=text.lower()       #lower case for whole text
print(text)

text=text.capitalize()  #upper case for first letter
print(text)

text=text.title()       #upper case for every word's first letter
print(text)

text='   Lorem ipsum dolar sit amet. Consectetur adipiscing elit'
text=text.strip()       #if there are some spaces beginning the text you can delete these space with strip() method
print(text)

text=text.split()       #split the text from the spaces and make it an array
print(text)
print(text[0])          #give the index number for calling array's component

text='Lorem ipsum dolar sit amet. Consectetur adipiscing elit'
text=text.split(".")    #also you can split the text with special character
print(text)
print(text[0])

text=' '.join(text)             #if you want to connect the text you can use join method
print(text)

text=text.split()
text='*'.join(text)             #also you can connect with special character
print(text)

index=text.find('ipsum')        #for finding a word in the text you can use find() method
print(index)

isStart=text.startswith("L")    #compare to starting with which letter or word
print(isStart)

isEnd=text.endswith("t")        #compare to ending with which letter or word
print(isEnd)

text='Lorem ipsum dolar sit amet. Consectetur adipiscing elit'
text=text.replace('ipsum','replaced')
print(text)

text=text.center(100)
print(text)

text='Lorem ipsum dolar sit amet. Consectetur adipiscing elit'
text=text.center(100,'*')
print(text)