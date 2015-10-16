import math
d=[45,338,19] #список диаметров
s=[] #объявляем список площадей
for i in d:
    pl=(math.pi*(i**2))/4
    s.append(pl) #добавляем элемент в конец списка
print(d)
print(s)
k=0
for i in range(len(s)): #ищем максимальную площадь, запоминаем номер элемента
    if s[i]>s[k]:
        k=i
r=s[k]
for i in range(len(s)): #вычитаем из максимальной площади все остальные
    if i!=k:
        r=r-s[i]
print(r)
    

