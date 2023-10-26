file=open('file.txt','w')
file.write('merhaba')
file.close
file=open('file.txt','a')
file.write('\nöğü öğü') #there is a problem about turkish letter characters
#we have to add encoding type to file that open file
file.close()
file=open('file.txt','a',encoding='utf-8')
file.write('\nöğü öğü')
file.close()