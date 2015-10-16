a=[1,-20,38,0,44]
b=[88,-20,48,4,33,2]
print(a)
print(b)
if len(a)<len(b):
    n=len(a)
else:
    n=len(b)
print(n, '- min number of elements') #количество элементов в меньшем списке
for i in range(n):
    if a[i]<b[i]:
        print(a[i])
        r=b[i]-a[i]
        if r<15:
            print('congrats, r =',r,'< 15')
            j=(i+r)%len(a) #вычисляем номер элемента в списке-победителе а, учитывая разницу r
            print(a[j])
    else:
        print(b[i])
        r=a[i]-b[i]
        if r<15:
            print('congrats, r =',r,'< 15')
            j=(i+r)%len(b) #вычисляем номер элемента в списке-победителе b, учитывая разницу r
            print(b[j])

        
