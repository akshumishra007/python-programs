class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
            a=self.length*self.breadth
            return  a

    def perimeter(self):
            p=2*(self.length+self.breadth)
            return p 

rect=[]
for i in range(2):
        length=int(input('enter length of rectangle '))
        breadth=int(input('enter breadth of rectangle ')) 
        w=rectangle(length,breadth) 
        rect.append(w)


def greater(r1,r2):
     if r1.area()>r2.area():
          print('the greater rectangle is: ',r1.area())

     elif r1.area()<r2.area():
        print('the greater rectangle is: ',r2.area())

     else:
          print('both rectangles have equal area')   


while True:
     print('CALCULATE AREA: 1')
     print('CALCULATE PERIMETER: 2')
     print('greater area of rectangle: 3')
     print('exit: 4')

     ch=int(input('enter your choice: '))

     if ch==1:
          for i in rect:
               print('area of rectangles:',i.area())


     elif ch==2:
           for i  in rect:
                print('perimeter of rectangles: ',i.perimeter())

     elif ch==3:
          greater(rect[0],rect[1])

     elif ch==4:
          print('thank you for ur input!!')
          break
     else:
          print('invalid input')        