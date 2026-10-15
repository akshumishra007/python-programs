import random
c=0
d=0
print('this is a rock paper scissor game enter your choise: r=rock, p=paper, s=scissor')
for i in range(5):
  user=input('enter your choise:')
  x=random.choice(['r','p','s'])
  if user==x:
    c+=0
    d+=0
    print('its a tie')
  elif user=='r' and x=='s':
    c+=1
    d+=0
    print('user wins')
  elif user=='p' and x=='r':
    c+=0
    d+=0
    print('user wins')
  elif user=='p' and x=='s':
    c+=0
    d+=1
    print('computer wins')
  elif user=='s' and x=='r':
    c+=0
    d+=1
    print('computer wins')
  else:
    print('invalid input')
    break
if c>d:
  print('user wins with a score of:',c)
elif d>c:
  print('computer wins with a score of:',d)
elif c==d:
  print('its a tie with a score of:',c)

