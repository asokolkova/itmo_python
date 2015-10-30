#coding: utf-8

def load_from_pickle(): #загрузка объекта из файла
    import pickle
    
    try:
        with open ('data.pickle','rb') as f:
            data = pickle.load(f)
        is_empty = False
    except Exception as e: #если объекта ещё нет
        print(type(e))
        print('Database is empty!')
        data = []
        is_empty = True
    else:
        print('Data base is not empty! ')
    finally:
        f.close()
    return data,is_empty

def save_to_pickle(data): #сохранение в pickle
    import pickle

    with open ('data.pickle','wb') as f:
        pickle.dump(data,f) #запись объекта в файл

    f.close()
