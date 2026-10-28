class counter:
    def __init__(self,count=0):
        self.count=count


    def increament(self):
        self.count+=1
        return self.count

    def decreament(self):
        if self.count !=0:
            self.count-=1
        else:
            print('counter already at zero cannot go lower')


    def reset(self):
       self.count =0
       return self.count


    def get_count(self):
        return self.count

c1=counter()
c2=counter(4)

while True:
 try:
    print('select anyone functions that u wish to perform')
    print('increase count: 1')
    print('decrease count: 2')
    print('reset counter: 3')
    print('print the current count: 4')
    print('exit: 5')
    ch=int(input('enter your choice: '))

    if ch==1:
            print(c1.increament())
            print(c2.increament())
    elif ch==2:
        c1.decreament()
        print(c1.get_count())
        c2.decreament()
        print(c2.get_count())

    elif ch==3:
        print(c1.reset())
        print(c2.reset())

    elif ch==4:
        print(c1.get_count())
        print(c2.get_count())

    elif ch==5:
       print('thank you for using this program!!')
       break

    else:
       print('invalid input')        
 except ValueError:
     print('please enter a valid number')
           
