import random 
x=random.randrange(1,100)
print('this is a guessing game you have to guess a number between 1 and 100.you have 6 chances to guess the right number')
for i in range(8):
  num=int(input('enter your guess:'))
  if num==x:
    print('you guessed it right')
  elif num>x:
    print('your guess is greater than the number')
  elif num<x:
    print('your guess is less than the number')

print('you ran out of chances to guess, the number was:', x)