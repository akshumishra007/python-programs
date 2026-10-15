print('enter your chosen operation: 1=adddition, 2=subtraction, 3=multiplication, 4=division, 5=modulus, 6=exponential')
op=int(input('enter operator number chosen'))
x=int(input('enter first number:'))
y=int(input('enter second number:'))
if op==1:
    print('sum is:', x+y)
elif op==2:
    print('difference is :', x-y)
elif op==3:
    print('product is:', x*y)
elif op==4:
    print('division is:', x/y)      
elif op==5:
    print('modulus is:', x%y)
elif op==6:
    print('exponential is:', x**y)
else:
    print('invalid operator')