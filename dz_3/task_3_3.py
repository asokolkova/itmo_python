import pickle
try:
    with open ('data.pickle','rb') as f:
        table_of_cars=pickle.load(f) #загружает объект из файла
except: #если объекта ещё нет
    table_of_cars=[]
fl=1 #будем вводить данные пока флаг не станет нулем
while fl!='0':
    operation=input('Enter operation: insert/out ')
    if operation=='insert':
        with open ('data.pickle','wb') as f: 
            model=input('Enter model of the car: ')
            power=input('Enter power ot the car: ')
            if (model.isalpha()==True) and (power.isdigit()==True):
                cars={}
                cars['model']=model
                cars['power']=power
                table_of_cars.append(cars)
                pickle.dump(table_of_cars,f) #запись объекта в файл
            else:
                print('Error! Model should contain only letters and power should contain only numbers')
    if operation=='out':
        with open ('data.pickle','rb') as f:
            table_of_cars=pickle.load(f)
            table_of_cars_sorted=table_of_cars[:]
            table_of_cars_sorted.sort(key=lambda i:i['model'])
            for i in range (len(table_of_cars_sorted)):
                print(table_of_cars_sorted[i]['model'],table_of_cars_sorted[i]['power'])
    fl=input('If you want to break and do another operation enter 0, if not - something else: ')

max_power=int(table_of_cars[0]['power'])
min_power=int(table_of_cars[0]['power'])
for i in range (len(table_of_cars)):
    if int(table_of_cars[i]['power'])>max_power:
        max_power=int(table_of_cars[i]['power'])
    if int(table_of_cars[i]['power'])<min_power:
        min_power=int(table_of_cars[i]['power'])
fl=int(input('If you want to find cars with power more than certain number print 1, less - print 2 and if you want to find cars with power between two numbers print 3: '))
if fl==1:
    k=int(input('Type the lowest power, all cars with power more than that will be printed: '))
    if k>=max_power:
        print('Nothing to print')
    else:
        for i in range (len(table_of_cars)):
            if int(table_of_cars[i]['power'])>k:
                print(table_of_cars[i]['model'],table_of_cars[i]['power'])
elif fl==2:
    k=int(input('Type the greatest power, all cars with power less than that will be printed: '))
    if k<=min_power:
        print('Nothing to print')
    else:
        for i in range (len(table_of_cars)):
            if int(table_of_cars[i]['power'])<k:
                print(table_of_cars[i]['model'],table_of_cars[i]['power'])
elif fl==3:
    s=input('Type two numbers, dividing them with ";", all cars with power between them will be printed: ')
    try:
        p=s.split(';')
        l=int(p[0])
        m=int(p[1])
        if (l>=max_power) or (m<=min_power):
            print('Nothing to print')
        else:
            for i in range (len(table_of_cars)):
                if l<int(table_of_cars[i]['power'])<m:
                    print(table_of_cars[i]['model'],table_of_cars[i]['power'])
    except:
        print('Error! You should divide two numbers with ";".') 
else:
    print('Error! Incorrect operation.')

fl=int(input('If you want to find cars with model containing certain string type 1, if you want to search by the whole name of the model type 2: '))
if fl==1:
    s=input('Enter string which the model should contain: ')
    fll=0
    for i in range (len(table_of_cars)):
        if s in table_of_cars[i]['model']:
            print(table_of_cars[i]['model'],table_of_cars[i]['power'])
            fll=1
    if fll==0:
        print('Nothing to print')
elif fl==2:
    s=input('Enter the model of the car: ')
    fll=0
    for i in range (len(table_of_cars)):
        if s==table_of_cars[i]['model']:
            print(table_of_cars[i]['model'],table_of_cars[i]['power'])
            fll=1
    if fll==0:
        print('Nothing to print')
else:
    print('Error! Incorrect operation.')

f.close()            
    
