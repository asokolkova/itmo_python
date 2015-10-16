table_of_stud=[]
file1=open('students.txt','r')
listf=file1.readlines()
listf=[s.rstrip() for s in listf]
for line in listf:
    parts=line.split('\t')
    stud=[]
    stud.append(parts[0])
    stud.append(parts[1])
    table_of_stud.append(stud)
file1.close()
print(table_of_stud)
n=len(table_of_stud)
print('We have',n,'students. Indexes 0 -',n-1) 
k=int(input('Please choose one of them, typing his index '))
print(table_of_stud[k][0]) #выводим только имя выбранного студента
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ')
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        print(table_of_stud[i][0])
elif l==m:
    print(table_of_stud[l][0])
else:
    for i in range (l,n,1):
        print(table_of_stud[i][0])
    for i in range (0,m+1,1):
        print(table_of_stud[i][0])
print('Students who have letter "р" in their names:')
k=0
for i in range (n):
    for el in table_of_stud[i][0]:
        if el=='р':
            k=k+1
            print(table_of_stud[i][0],table_of_stud[i][1])
print('We have',k,'students who have letter "р" in their names.')
table2=[]
table_copy=table_of_stud[:] #скопировали исходный список студентов, из него удаляем студентов с повторяющимися именами
i=0
while i < len(table_copy)-1:
    j=i+1
    s=table_copy[i][0]
    while j < len(table_copy):
        if table_copy[j][0]==s:
            table2=table_copy.pop(j)
        else:
            j=j+1
    i=i+1
print('Students with different names: ')
print(table_copy)#в итоге в table_copy останутся только студенты с разными именами
group=[] #идём по именам в списке table_copy, найденные такие же имена в table_of_stud записываем в новый список new_stud 
for j in range (len(table_copy)):
    new_stud=[]
    for i in range (n):
        if table_copy[j][0]==table_of_stud[i][0]:
            new_stud.append(table_of_stud[i])
    group.append(new_stud) #списки студентов с одинаковыми именами записываем в новый список group
print('Groups of student"s with the same names: ')
print(group)

print('We have',n,'students. Indexes 0 -',n-1) 
k=int(input('Please choose one of them, typing his index '))
table_log=[]
file2=open('students.log','r')
listf=file2.readlines()
listf=[s.rstrip() for s in listf]
for line in listf:
    parts=line.split('\t')
    stud_log=[]
    stud_log.append(parts[0])
    stud_log.append(parts[1])
    stud_log.append(parts[2])
    table_log.append(stud_log)
file2.close()
for i in range(len(table_log)):
    if (table_log[i][0]==table_of_stud[k][0]) and (table_log[i][1]==table_of_stud[k][1]):
        print(table_log[i][0],table_log[i][1],table_log[i][2]) #выводим студента и действие из log файла
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ') #то же самое для нескольких студентов
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
elif l==m:
    for i in range(len(table_log)):
        if (table_log[i][0]==table_of_stud[l][0]) and (table_log[i][1]==table_of_stud[l][1]):
            print(table_log[i][0],table_log[i][1],table_log[i][2])
else:
    for i in range (l,n,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
    for i in range (0,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ') #для нескольких студентов, но будем выводить только тех студентов, которые что-то скачали
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]) and ('download' in table_log[j][2]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
elif l==m:
    for i in range(len(table_log)):
        if (table_log[i][0]==table_of_stud[l][0]) and (table_log[i][1]==table_of_stud[l][1]) and ('download' in table_log[j][2]):
            print(table_log[i][0],table_log[i][1],table_log[i][2])
else:
    for i in range (l,n,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]) and ('download' in table_log[j][2]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
    for i in range (0,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]) and ('download' in table_log[j][2]):
                print(table_log[j][0],table_log[j][1],table_log[j][2])
   






