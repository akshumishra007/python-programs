print('enter marks abtained in all subjects')
total=0
x=int(input('no of subjects: '))
for i in range(x):
    marks=int(input('marks in subject: '))
    total+=marks
avg=total/x
try:
  if avg>90:
    print('grade is A')
  elif avg>80:
    print('grade is B')     
  elif avg>70:
    print('grade is C')
  elif avg>60:
    print('grade is D') 
  else:
    print('grade is F')

except ZeroDivisionError:
  print('no subjects entered')

