f=1 #будем вводить данные пока флаг не станет нулем
while f!=0:
    x=int(input('Enter the first number: '))
    y=int(input('Enter the second number: '))
    op=input('Enter operation (+,-,*,/,//,%,**): ')
    k=1 #флаг, что была введена корректная операция
    if op=='+':
        z=x+y
    elif op=='-':
        z=x-y
    elif op=='*':
        z=x*y
    elif op=='/':
        z=x/y
    elif op=='//':
        z=x//y
    elif op=='%':
        z=x%y
    elif op=='**':
        z=x**y
    else:
        print('Warning! Incorrect operation. Try again.')
        k=0
    if k==1:
        print(x,op,y,'=',z)
    f=int(input('If you want to break enter 0: '))

