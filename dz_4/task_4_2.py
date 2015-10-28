#coding: utf-8

def load_from_pickle(): #загрузка объекта из файла

    import pickle

    try:
        with open ('data_nomer_coord.pickle','rb') as f:
        
            data = pickle.load(f)

    except: #если объекта ещё нет
        data = []

    f.close()

    return data

def save_to_pickle(data): #сохранение в pickle

    import pickle

    with open ('data_nomer_coord.pickle','wb') as f:
        
        pickle.dump(data,f) #запись объекта в файл

    f.close()

def inter_operation(): #ввод операции

    op = input('Enter operation: insert/out/search power/search model/edit car/delete car/move car: ')

    return op

def incorrect_operation(): #сообщение в случае ошибки ввода комманды

    print('Error! Incorrect operation.') 

def insert_cars(): #ввести данные в базу данных
    
    data = load_from_pickle()

    model = input('Enter model of the car: ')
    power = input('Enter power ot the car: ')
    sign = input('Enter sign of the car: ')           # * 4.4 - добавляем номерной знак и координаты относительно автобазы
    coord_x = input('Enter coord x ot the car: ')
    coord_y = input('Enter coord y ot the car: ')

    if (model.isalpha() == True) and (power.isdigit() == True) and (coord_x.isdigit() == True) and (coord_y.isdigit() == True):
        
        cars = {}
        cars['model'] = model
        cars['power'] = power
        cars['sign'] = sign
        cars['x'] = coord_x
        cars['y'] = coord_y
        data.append(cars)

        save_to_pickle(data)

    else:
        print('Error! Model should contain only letters; power, coordinats should contain only numbers and sign should contain only numbers and letters.')

def out_cars(): #напечатать содержимое базы данных

    data = load_from_pickle()
    fl = 0

    data_sorted = data[:]
    data_sorted.sort(key=lambda i:i['model'])

    for i in range (len(data_sorted)): # выводим автомобили по алфавиту
        print(data_sorted[i]['model'],data_sorted[i]['power'],data_sorted[i]['sign'],data_sorted[i]['x'],data_sorted[i]['y'])

        fl = 1

    if (fl == 0):
        print('Database is empty!')

def search_max_min_p(data): #определяем макс и мин мощность

    max_power = int(data[0]['power'])
    min_power = int(data[0]['power'])

    for i in range (len(data)):
        
        if int(data[i]['power']) > max_power:
            max_power = int(data[i]['power'])

        if int(data[i]['power']) < min_power:
            min_power = int(data[i]['power'])

    return max_power, min_power

def search_more_p(data,max_power): #поиск по мощности - больше конкретного числа

    k = input('Type the lowest power, all cars with power more than that will be printed: ')
    
    if int(k) >= max_power:
        print('Nothing to print')

    else:
        for i in range (len(data)):

            if int(data[i]['power']) > int(k):
                print(data[i]['model'],data[i]['power'],data[i]['sign'],data[i]['x'],data[i]['y'])

def search_less_p(data,min_power): #поиск по мощности - меньше конкретного числа

    k = input('Type the greatest power, all cars with power less than that will be printed: ')

    if int(k) <= min_power:
        print('Nothing to print')

    else:
        for i in range (len(data)):

            if int(data[i]['power']) < int(k):
                print(data[i]['model'],data[i]['power'],data[i]['sign'],data[i]['x'],data[i]['y'])    

def search_middle_p(data,min_power,max_power): #поиск по мощности - в промежутке 2ух введенных чисел

    s = input('Type two numbers, dividing them with ";", all cars with power between them will be printed: ')

    try:

        p = s.split(';')
        l = int(p[0])
        m = int(p[1])

        if (l >= max_power) or (m <= min_power):
            print('Nothing to print')

        else:

            for i in range (len(data)):

                if l < int(data[i]['power']) < m:
                    print(data[i]['model'],data[i]['power'],data[i]['sign'],data[i]['x'],data[i]['y'])

    except:
        print('Error! You should divide two numbers with ";".')       

def search_p(): #поиск по мощности

    data = load_from_pickle()
    
    try:

        max_power, min_power = search_max_min_p(data)

        fl = input('If you want to find cars with power more than certain number print 1, less - print 2 and if you want to find cars with power between two numbers print 3: ')

        if fl == '1':
            search_more_p(data,max_power)

        elif fl == '2':
            search_less_p(data,min_power)
        
        elif fl == '3':
            search_middle_p(data,min_power,max_power)

        else:
            incorrect_operation()

    except:
        print('Database is empty!')
        
def search_str_in_m(data): #по вхождению слова в название

    s = input('Enter string which the model should contain: ')
    fl = 0

    for i in range (len(data)):

        if s in data[i]['model']:

            print(data[i]['model'],data[i]['power'],data[i]['sign'],data[i]['x'],data[i]['y'])
            fl = 1

    if fl == 0:
        print('Nothing to print')

def search_model(data): #по полному соответствию слова

    s = input('Enter the model of the car: ')
    fl = 0

    for i in range (len(data)):

        if s == data[i]['model']:

            print(data[i]['model'],data[i]['power'],data[i]['sign'],data[i]['x'],data[i]['y'])
            fl = 1

    if fl == 0:
        print('Nothing to print')

def search_m(): #поиск по названию

    data = load_from_pickle()

    try:

        fl = input('If you want to find cars with model containing certain string type 1, if you want to search by the whole name of the model type 2: ')

        if fl == '1':
            search_str_in_m(data)
        
        elif fl == '2':
            search_model(data)

        else:
            incorrect_operation()

    except:
        print('Database is empty!')

def search_op_dict(): #4.2 поиск операции в словаре и запуск функции по ключу словаря

    operation = inter_operation()

    funcs = {'insert': insert_cars, 'out': out_cars, 'search power': search_p, 'search model': search_m, 'edit car': edit, 'delete car': delete, 'move car': move}

    keys = list(funcs.keys())
    fl = 0

    for i in keys:

        i = str(i)

        if i == operation:
            fl = 1
            
            funcs[i]()

    if fl == 0:
        incorrect_operation()

def edit(): #4.3 редактирование

    data = load_from_pickle()

    try:

        s = input('Type sign of the car you want to edit: ')
        fl = 0

        for i in range (len(data)):

            if (data[i]['sign'] == s):

                fl = 1

                k = input('If you want to change model of the car type 1, if power - type 2: ')

                if k == '1':

                    new_m = input('Enter new model of the car: ')

                    if (new_m.isalpha() == True):
                                
                        data[i]['model'] = new_m
                        save_to_pickle(data)

                    else:
                        print('Error! Model should contain only letters.')

                elif k == '2':

                    new_p = input('Enter new power ot the car: ')

                    if (new_p.isdigit() == True):

                        data[i]['power'] = new_p
                        save_to_pickle(data)

                    else:
                        print('Error! Power should contain only numbers.')

                else:
                    incorrect_operation()

        if fl == 0:
            print('There is no such car in database')

    except:
        print('Database is empty!')

def delete(): #4.3 удалить машину из БД

    data = load_from_pickle()

    try:
    
        s = input('Type sign of the car you want to delete: ')

        fl = 0
        data_pop = []

        for i in range (len(data)):

            if (data[i]['sign'] == s):

                fl = 1
                data_pop = data.pop(i)

                save_to_pickle(data)

        if fl == 0:
            print('There is no such car in database')

    except:
        print('Database is empty!')    

def move(): # *4.4 выбрать автомобиль по номеру и переместить в другие координаты

    data = load_from_pickle()

    try:

        s = input('Type sign of the car you want to move: ')
        fl = 0

        for i in range (len(data)):

            if (data[i]['sign'] == s):

                fl = 1

                new_x = input('Enter new x coord of the car: ')
                new_y = input('Enter new y coord of the car: ')

                if (new_x.isdigit() == True) and (new_y.isdigit() == True):

                    flag = 0

                    for j in range (len(data)):

                        if (data[j]['x'] == new_x) and (data[j]['y'] == new_y):
                            flag = 1

                    if (flag == 0) or (new_x == '0' and new_y == '0'): # *4.5 система не позволяет поставить 2 автомобиля в одинаковые координаты, но в автобазе (0,0) могут стоять все машины

                        old_x = data[i]['x']
                        old_y = data[i]['y']

                        data[i]['x'] = new_x
                        data[i]['y'] = new_y

                        import math
                        d = math.sqrt((int(new_x) - int(old_x))**2+(int(new_y) - int(old_y))**2) # *4.6 считаем расстояние, которое проехал автомобиль
                        print('Distance is: ', str(d))

                        save_to_pickle(data)

                    else:
                        print("You can't move car here, the place is taken.")

                else:
                    print('Error! Coordinates should contain only numbers.')

        if fl == 0:
            print('There is no such car in database')

    except Exception:
        print('Database is empty!')


# основная программа

flag = 1 #будем вводить/выводить данные пока флаг не станет нулем

while flag != '0':

    search_op_dict() #4.2 поиск операции в словаре и запуск функции по ключу словаря

    flag = input('If you want to break enter 0, if not - something else: ')


        
    
