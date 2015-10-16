import math
file1=open('input_1_2.txt','r')
numbers=file1.readlines() #список из строк
numbers=[s.rstrip() for s in numbers] #убираем символ перевода строки
file1.close()
print(numbers)
x=int(numbers[0])+int(numbers[1])
print(numbers[0],'+',numbers[1],'=',x)
y=math.sqrt(int(numbers[2])*int(numbers[3]))
print('sqrt','(',numbers[2],'*',numbers[3],')','=',y)
if x>y:
    print(x,'>',y)
elif x==y:
    print(x,'=',y)
else:
    print(y,'>',x)
z=math.cos(int(numbers[4]))
print('cos','(',numbers[4],')','=',z)

    
