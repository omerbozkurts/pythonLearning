#q1 delete the spaces to beginning and ending from " Hello World " text

text= ' Hello World '
text= text.strip()
print(text)

#q2 delete everything from www.github.com not including github

text='www.github.com'
text=text.split('.')
text=text[1]
print(text)

#q3 make lower case whole text 'CoUrSE'

text='CoUrSE'
text=text.lower()
print(text)

#q4 how many a character in 'website' text

text='wwww.github.com/programming'
count=text.count('a')
print(count)

#q5 is 'website' start with www and end with com

text='www.github.com'
isStart=text.startswith('www')
isEnd=text.endswith('com')
print(f'the text is start with www: {isStart} \nthe text is end with com: {isEnd}')

#q6 is there com in 'website' text

text='www.github.com'
isThere=text.find('com')
print('is there com: {}'.format(isThere))

#q7 make 50 space from left side and right side to 'Contents' text and place the '*' character left and right sides

text='Contents'
text=text.center(50,'*')
print(text)

#q8 replace the space with - character in the text

text='Lorem ipsum dolar sit amet'
text=text.replace(' ','-')
print(text)

#q9 are whole characters alphabetic in the text

text='Lorem'
result=text.isalpha()
print(result)
text= '3415'
result=text.isdigit()
print(result)