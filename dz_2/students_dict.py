table_of_stud=[]
file1=open('students_dict.txt','r')
listf=file1.readlines()
listf=[s.rstrip() for s in listf]
for line in listf:
    parts=line.split('\t')
    stud={}
    stud['name']=parts[0]
    stud['fam']=parts[1]
    stud['year']=parts[2]
    table_of_stud.append(stud)
file1.close()
print(table_of_stud)
n=len(table_of_stud)
print('We have',n,'students. Indexes 0 -',n-1) 
k=int(input('Please choose one of them, typing his index '))
print(table_of_stud[k]['name'],table_of_stud[k]['year']) #выводим имя и возраст выбранного студента
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ')
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        print(table_of_stud[i]['name'], table_of_stud[i]['year'])
elif l==m:
    print(table_of_stud[l]['name'], table_of_stud[l]['year'])
else:
    for i in range (l,n,1):
        print(table_of_stud[i]['name'], table_of_stud[i]['year'])
    for i in range (0,m+1,1):
        print(table_of_stud[i]['name'], table_of_stud[i]['year'])
print('Students who have letter "р" in their names:')
k=0
for i in range (n):
    for el in table_of_stud[i]['name']:
        if el=='р':
            k=k+1
            print(table_of_stud[i]['name'], table_of_stud[i]['fam'], table_of_stud[i]['year'])
print('We have',k,'students who have letter "р" in their names.')
table2=[]
table_copy=table_of_stud[:] #скопировали исходный список студентов, из него удаляем студентов с повторяющимися именами
i=0
while i < len(table_copy)-1:
    j=i+1
    s=table_copy[i]['name']
    while j < len(table_copy):
        if table_copy[j]['name']==s:
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
        if table_copy[j]['name']==table_of_stud[i]['name']:
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
    stud_log={}
    stud_log['name']=parts[0]
    stud_log['fam']=parts[1]
    stud_log['act']=parts[2]
    table_log.append(stud_log)
file2.close()
for i in range(len(table_log)):
    if (table_log[i]['name']==table_of_stud[k]['name']) and (table_log[i]['fam']==table_of_stud[k]['fam']):
        print(table_log[i]['name'],table_log[i]['fam'],table_of_stud[k]['year'],table_log[i]['act']) #выводим студента и действие из log файла
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ') #то же самое для нескольких студентов
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j]['name']==table_of_stud[i]['name']) and (table_log[j]['fam']==table_of_stud[i]['fam']):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
elif l==m:
    for i in range(len(table_log)):
        if (table_log[i]['name']==table_of_stud[l]['name']) and (table_log[i]['fam']==table_of_stud[l]['fam']):
            print(table_log[i]['name'],table_log[i]['fam'],table_of_stud[l]['year'],table_log[i]['act'])
else:
    for i in range (l,n,1):
        for j in range(len(table_log)):
            if (table_log[j]['name']==table_of_stud[i]['name']) and (table_log[j]['fam']==table_of_stud[i]['fam']):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
    for i in range (0,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j][0]==table_of_stud[i][0]) and (table_log[j][1]==table_of_stud[i][1]):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
s=input('Please choose several students, type first and last indexes, dividing two numbers with ";" ') #для нескольких студентов, но будем выводить только тех студентов, которые что-то скачали
p=s.split(';')
l=int(p[0])
m=int(p[1])
if l<m:
    for i in range (l,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j]['name']==table_of_stud[i]['name']) and (table_log[j]['fam']==table_of_stud[i]['fam']) and ('download' in table_log[j]['act']):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
elif l==m:
    for i in range(len(table_log)):
        if (table_log[i]['name']==table_of_stud[l]['name']) and (table_log[i]['fam']==table_of_stud[l]['fam']) and ('download' in table_log[j]['act']):
            print(table_log[i]['name'],table_log[i]['fam'],table_of_stud[l]['year'],table_log[i]['act'])
else:
    for i in range (l,n,1):
        for j in range(len(table_log)):
            if (table_log[j]['name']==table_of_stud[i]['name']) and (table_log[j]['fam']==table_of_stud[i]['fam']) and ('download' in table_log[j]['act']):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
    for i in range (0,m+1,1):
        for j in range(len(table_log)):
            if (table_log[j]['name']==table_of_stud[i]['name']) and (table_log[j]['fam']==table_of_stud[i]['fam']) and ('download' in table_log[j]['act']):
                print(table_log[j]['name'],table_log[j]['fam'],table_of_stud[i]['year'],table_log[j]['act'])
