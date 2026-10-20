import random
print('lets create a password')
n=int(input('enter the length for your password:'))
password=''
if n>0: 
 x=input('do you want the password to contain uppercase letter y/n: ').strip()
 y=input('do you want the password to contain special characters y/n: ').strip() 
 z=input('do you want the password to contain numbers y/n: ').strip()
 a=input('do you want the password to contain lowercase letter y/n: ').strip()
 for i in range(n):    
    if x=='y'and y=='y' and z=='y' and a=='y':
        password+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*')
    elif y=='y' and z=='y' and x=='y':
        password+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*') 
    elif x=='y' and z=='y' and a=='y':
        password+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    elif x=='y' and y=='y' and a=='y':
        password+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*')
    elif a=='y' and y=='y' and z=='y':               
        password+=random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*')
 else:
        print('invalid choice')
 print('your random generated password is :',password)
else:
    print('invalid length') 

