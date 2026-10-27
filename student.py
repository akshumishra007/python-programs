class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no =roll_no
        self.marks= marks


    def avg(self):

     x=sum(self.marks)/len(self.marks)
     print('average marks of student:',x)

    def display(self):
        print('name:',self.name)
        print('roll no:',self.roll_no)
        print('marks:',self.marks)
        print('-------------------------')


num=int(input ('how many students do u wish to enter'))
students=[]
for i in range(num):
      l=[]
      name=input('enter name of the student')
      roll_no=int(input('enter roll no'))
      sub=int(input('enter number of subjects : '))

      for i in range(sub):
         marks=int(input('enter marks of each subject: '))
         l.append(marks)
      s=student(name,roll_no,l)
      students.append(s)   
   

while True:      
   print('CALCULATE AVERAGE: 1')
   print('DISPLAY THE STUDENTS :2')
   print('exit: 3')
   ch=int(input('enter your choice:'))

   if ch==1:
      for s in students:
       s.avg()

   elif ch== 2:
      for s in students:
       s.display()

   elif ch==3:
      print('thank you for using !!')
      break
   else:
      print('enter a valid choice')

   