t=int(input('enter temperature :'))
unit=input('enter unit of temperature (c/f):')
if unit=='c':
    f=(t*9/5)+32
    print('temperature in farenheit is :', f)
elif unit=='f':
    c=(t-32)*5/9
    print('temperature in celsius is :', c)
else:
    print('invalid unit')