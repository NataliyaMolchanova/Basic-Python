# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

# from itertools import cycle
# from time import sleep
#
#
# class Traffic:
#     colors_queue = ("красный", "желтый", "зеленый")
#     time_queue = (7, 2, 5)
#     message = ("Красный — движение запрещено", "Желтый — скоро включится зеленый", "Зеленый — движение разрешено")
#
#     def __init__(self, color):
#         self.__color = color
#
#     def running(self):
#         my_cycle = cycle(self.colors_queue)
#         for traffic_color in my_cycle:
#             if self.__color == traffic_color:
#                 print(self.message[self.colors_queue.index(self.__color)])
#                 sleep(self.time_queue[self.colors_queue.index(self.__color)])
#                 self.__color = next(my_cycle)
#
# my_traffic = Traffic("красный")
# my_traffic.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# class Road:
#     def __init__(self, width, length):
#         self.width = width
#         self.lenght = length
#
#     def asphalt(self, weight_ratio, thikness):
#         asphalt = self.lenght * self.width * weight_ratio * thikness
#         return asphalt
#
#
# my_road = Road(20, 5000)
# print(my_road.asphalt(25, 5))



# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#
#     def get_full_mane(self):
#         return f"{self.name} {self.surname} {self.position}"
#
#     def get_full_salary(self):
#         return self._income['wage'] + self._income['bonus']
#
# my_position = Position('Вася', 'Галочкин', 'тестировщик', 100000, 20000)
# print(f'Данные о сотруднике {my_position.get_full_mane()} : {my_position.get_full_salary()}')


#
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
# #
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print(f"Машина {self.color} цвета, марки {self.name}, едет со скоростью {self.speed}")
#
#     def stop(self):
#         print(f"Машина {self.color} цвета, марки {self.name}, сделала остановку")
#
#     def turn(self, direction):
#         print(f"Машина {self.color} цвета, марки {self.name}, повернула на {direction}")
#
#     def show_speed(self):
#         print(f"Скорость машины {self.speed}")
#
# class Towncar(Car):
#
#     def show_speed(self):
#         if self.speed > 60:
#             print("Превышение! Снизьте скорость до 60 км/ч")
#
# class SportCar(Car):
#
#     def __init__(self, speed, color, name):
#         Car.__init__(self, speed, color, name, is_police=False)
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         if self.speed > 40:
#             print("Превышение! Снизьте скорость до 40 км/ч")
#
# class PoliceCar(Car):
#
#     def __init__(self, speed, color, name):
#         Car.__init__(self, speed, color, name, is_police=True)
#
# my_policecar = PoliceCar(110, "черного", "BMW")
# my_policecar.go()
# my_policecar.turn("право")
# my_policecar.stop()
# my_policecar.show_speed()
#
# my_workcar = WorkCar(44, "белого", "Renault Logan", False)
# my_workcar.go()
# my_workcar.turn("право")
# my_workcar.stop()
# my_workcar.show_speed()
#
# my_sportcar = SportCar(200, "красного", "Lamborgini Diablo")
# my_sportcar.go()
# my_sportcar.turn("право")
# my_sportcar.stop()
# my_sportcar.show_speed()
#
# my_towncar = Towncar(66, "белого", "Mini", False)
# my_towncar.go()
# my_towncar.turn("лево")
# my_towncar.stop()
# my_towncar.show_speed()


#
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

# class Stationery:
#     title = "Stationery"
#
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationery):
#     title = "Pen"
#
#     def draw(self):
#         print('Запуск отрисовки ручкой')
#
# class Pencil(Stationery):
#     title = "Pencil"
#
#     def draw(self):
#         print('Запуск отрисовки карандашом')
#
# class Handle(Stationery):
#     title = "Handle"
#
#     def draw(self):
#         print('Запуск отрисовки маркером')
#
# pen = Pen()
# pencil = Pencil()
# handle = Handle()
# pen.draw()
# pencil.draw()
# handle.draw()