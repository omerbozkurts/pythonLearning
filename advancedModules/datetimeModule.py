# import datetime
# from datetime import date
# from datetime import time

from datetime import datetime

rNow = datetime.now()

print(rNow)

rNowYear = rNow.year

print(rNowYear)

rNowDay= rNow.day

print(rNowDay)

print(datetime.ctime(rNow))

print(datetime.strftime(rNow,'%Y'))

print(datetime.strftime(rNow,'%X'))

print(datetime.strftime(rNow,'%D'))

print(datetime.strftime(rNow,'%M'))

t = '15 August 2002 hour 04:29:32'

tF = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')

print(tF)
print(tF.day)


birthDay = datetime(2000,10,15,18,36,13)

print(datetime.timestamp(birthDay)) # writes time information as second

print(datetime.fromtimestamp(0))