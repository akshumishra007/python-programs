
contact={}
def add_con():
    name =input('enter the name for contact:')
    phone =input('enter the phone no: ')
    if len(phone)==10 and phone.isdigit():
      contact[name]=phone
      print('contact added successfully')
    else:
       print('pls enter a valid contact number')

def del_con():
   x=input('enter the contact name you wish to delete: ')
   if x in contact:
    del contact[x]
    print('contact deleted successfully!') 
   else:
      print('enter a valid contact name')

def display_dic():
   print('CONTACT BOOK')
   for i in contact:
     print('name:',i )
     print('phone no:',contact[i])

def search_con():
   x=input('enter the contact you wish to search: ')  
   if x in contact:
      print('CONTACT' )
      print( 'name:', x )
      print('phone:',contact[x])
   else:
      print('invalid contact') 

while True:
 print('---------------------------')
 print('       CONTACT BOOK')
 print('---------------------------')
 print('select whichever function u want to add to your contacts')
 print('1.add a contact')
 print('2.delete a contact' )
 print('3.display the contact list' )
 print('4.search for a contact')
 print('5.exit the contact book')
 ch=int(input('enter your choice of the 4 choices : '))
 if ch==1:
  add_con()
 elif ch==2:
  del_con()
 elif ch==3:
  display_dic()
 elif ch==4:
  search_con()
 elif ch==5:
   print('thank you for using the contact book')
   break
 else:
   print('enter a valid choice')
