import re 

#print(dir(re))

txt = "Hello World. It's a Python File for Regular Expression"

print(re.findall('World',txt))

print(re.split('\s',txt))

print(re.sub('File','Course',txt))

print(re.search('for',txt))

searchObject  = re.search('for',txt)

print(searchObject.span())

print(searchObject.start())

print(searchObject.end())

print(searchObject.group())

print(re.findall("[abc]",txt))