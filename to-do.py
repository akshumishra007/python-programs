print('create your own to-do list')
l=[]
y=int(input('enter length of list'))
for i in range (y):
  z=input('enter value')
  l.append(z)
print('what do u want to do today?')
print('1. add a task')
print('2. view tasks')  
print('3. remove a task')
print('4. mark a task as done')
ch=int(input('enter your choice:'))
if ch==1:
  task=input('enter your task:').strip()
  l.append(task)
  print('task added successfully')
elif ch==2:
  print('your tasks are:')
  for i in l:
    print(i,end=', ')
elif ch==3:
  t=input('enter the task you want to remove:').strip()
  l.remove(t)
  print('task removed successfully')
elif ch==4:
   t=input('enter the task you want to mark as done:').strip()
   x=l.index(t)
   l[x]= t +': done'
   print(l)
else:
  print('invalid choice')
