print('---------------------------------')
print('PYTHON QUIZ')
print('---------------------------------')
print('this is a quiz based on python programming')
print('you will be asked 5 questions and you have to answer them correctly')
x=str(input('enter your name:'))
print('hello', x) 
print('good luck for the quiz!')
c=0
dict={'who developed python?':'C','what symbol is used for comments in python?':'A','what is the output of 2**3?':'B','what is the output of 5/2?':'B','what datatype is used to store text?':'C'}
L=['(A) James Gosling,(B) Dennis Ritchie,(C) Guido van Rossum,(D) Bjarne Stroustrup', '(A) "#", (B) //, (C) /*, (D) "$" ', '(A) 6, (B) 8, (C) 9, (D) 10', '(A) 2, (B) 2.5, (C) 3, (D) 4', '(A) int, (B) float, (C) str, (D) bool']
for i in dict:
    print(i)
    print(L[0])
    L.remove(L[0])                                                          
    ans=str(input('enter your answer:')).upper()
    if ans==dict[i]:    
        print('correct answer')
        c+=1
    else:
        print('wrong answer')
    
print('the quiz is finished')
per=(c/5)*100
print('name:', x)
print('final score is ',c,'/5')
print('percentage is:', per,'%')

print('thank you for playing the quiz!')