from datetime import datetime

def timedate(a,b):
   timeA = datetime.strptime(a, "%m%d,%H:%M")
   timeB = datetime.strptime(b, "%m%d,%H:%M")
   timeDiff = timeB - timeA
   
   return timeDiff

a = ''
def timeConversion(s):
   if FstTimeFormat == '1' or SecTimeFormat == '1':
       a = s
   elif FstHourFormat == 'AM' or SecHourFormat == 'AM' :
      if s[5:7] == '12':
          a = str(s[:5] + '00' + s[7:10])
      else:
          a = s
   else :
       a = str( s[:5] + int(s[5:7]) + 12) + s[7:10]
       print('this is a:',a)
   return a



FstTimeFormat = input('Time format? (1: 24hr / 2: 12hr)')
FstDate = input('1st Date? (e.g. 0605)')
FstHourFormat = input('(if 24hr, skip this) 1st AM/PM?')
FstTime = input('1st Time? (e.g. 17:30 or 05:30)')
SecTimeFormat = input('Time format? (1: 24hr / 2: 12hr)')
SecDate = input('2nd Date? (e.g. 0605)')
SecHourFormat = input('(if 24hr, skip this) 1st AM/PM?')
SecTime = input('2nd Time? (e.g. 17:30 or 05:30)')

FstDateTime = FstDate +','+ FstTime
SecDateTime = SecDate +','+ SecTime

conversionFstDateTime = timeConversion(FstDateTime)
conversionSecDateTime = timeConversion(SecDateTime)

Result = str(timedate(conversionFstDateTime,conversionSecDateTime))

Result = Result.replace(' day, ',':').replace(':',' ')
print('Result:',Result)


#先從日期開始解，再用24時區解
#要怎麼編輯strp時間格式
#想到直接合併string來帶入strp
