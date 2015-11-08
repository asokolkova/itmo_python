#coding: utf-8

class Tank: # 1. класс Танк (модель=строка, шасси=False/True, скорость=число, гусеницы=False/True)

    def __init__(self):
        self.model = 'T34'
        self.shassi = True
        self.gus = True
        self.speed = 50

    def status(self): # 2. метод status, выводящий состояние объекта на данный момент
        if self.shassi == True and self.gus == True and self.speed > 0:
            print('Tank',self.model,'going')
        else:
            print('Tank',self.model,'not going')
            
class Car: # 1. класс Машина (модель, колеса, скорость)

    def __init__(self):
        self.model = 'Audi'
        self.wheels = 4
        self.speed = 60

    def status(self): # 2. метод status, выводящий состояние объекта на данный момент
        if self.wheels >= 4 and self.speed > 0:
            print('Car',self.model,'going')
        else:
            print('Car',self.model,'not going')

class Telega: # 1. класс Телега (колеса, скорость)

    def __init__(self):
        self.wheels = 4
        self.speed = 10

    def status(self): # 2. метод status, выводящий состояние объекта на данный момент
        if self.wheels >= 4 and self.speed > 0:
            print('Telega','going')
        else:
            print('Telega','not going')

# 3. Создаем и собираем сколько-то новых объектов этих классов в список cars
tank1 = Tank()
tank2 = Tank()
car1 = Car()
car2 = Car()
telega1 = Telega()

# 4. Делаем несколько действий с этими объектами (Например, назначили машине "Audi" скорость 90, у танка 'Т34' сняли шасси)
tank1.shassi = False
tank2.model = 'Tiger'
car1.speed = 90
car2.model = 'Ford'
telega1.wheels = 2

# 5. В конце программы выводим состояния всех объектов из cars
cars = [tank1,tank2,car1,car2,telega1]
for el in cars:
    el.status()
