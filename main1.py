### Зад.1. Создайте класс Device, который содержит информацию об устройстве. С помощью механизма наследования,
# реализуйте класс CoffeeMashine (содержит и нформацию о кофемашине), класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке). Каждый из классов должен содержать необходимые для работы методы.

# from abc import ABC, abstractmethod
#
#
# class Device(ABC):
#
#     def __init__(self, manufacturer, guarantee, country, price):
#         self.manufacturer = manufacturer
#         self.guarantee = guarantee
#         self.country = country
#         self.price = price
#
#     def get_info(self):
#
#         return f'{self.name}. Фирма-производитель - {self.manufacturer}. ' \
#                f'Гарантия производителя составляет {self.guarantee}. ' \
#                f'Страна-производитель - {self.country}. ' \
#                f'Цена - {self.price}'
#
#     @abstractmethod
#     def name(self):
#         pass
#
#     @abstractmethod
#     def advantages(self):
#         pass
#
#
# class CoffeeMashine(Device):
#     @property
#     def name(self):
#         return 'Кофемашина'
#
#     def advantages(self):
#         print('легкий для пользователя процесс кофеварения')
#
#
# class Blender(Device):
#     @property
#     def name(self):
#         return 'Блендер'
#
#     def advantages(self):
#         print('легкий для пользователя процесс взбивания и размельчения')
#
#
# class MeatGrinder(Device):
#     @property
#     def name(self):
#         return 'Мясорубка'
#
#     def advantages(self):
#         print('функциональность за счет различных насадок, необходимых для приготовления разнообразных блюд')
#
#
# c = CoffeeMashine('Garlyn', '2 года', 'Германия', '20000 руб.')
# print(c.get_info())
# c.advantages()
# print('--------------')
#
# a = Blender('Moulinex', '1 год', 'Китай', '5000 руб.')
# print(a.get_info())
# a.advantages()
# print('--------------')
#
# b = MeatGrinder('Panasonic', '1 год', 'Китай', '13000 руб.')
# print(b.get_info())
# b.advantages()



### Зад.2. Создайте класс Ship, который содержит информацию о корабле. С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс Destroyer (содержит информацию об эсминце), класс Cruiser
# (содержит информацию о крейсере). Каждый из классов должен содержать необходимые для работы методы.

# from abc import ABC, abstractmethod
#
#
# class Ship(ABC):
#
#     def __init__(self, load_capacity, speed, cruising_range):
#         self.load_capacity = load_capacity
#         self.speed = speed
#         self.cruising_range = cruising_range
#
#     def get_info(self):
#
#         return f'{self.type}. Грузоподъемность - {self.load_capacity} тонн. ' \
#                f'Скорость - {self.speed} км/ч. ' \
#                f'Дальность плавания - {self.cruising_range} миль. '
#
#     @abstractmethod
#     def type(self):
#         pass
#
#     @abstractmethod
#     def advantages(self):
#         pass
#
#
# class Frigate(Ship):
#     @property
#     def type(self):
#         return 'Фрегат'
#
#     def advantages(self):
#         print('Тип военного судна. Трехмачтовый парусный корабль')
#
#
# class Destroyer(Ship):
#     @property
#     def type(self):
#         return 'Эсминец'
#
#     def advantages(self):
#         print('Боевой корабль, предназначенный для борьбы с подводными лодками')
#
#
# class Cruiser(Ship):
#     @property
#     def type(self):
#         return 'Крейсер'
#
#     def advantages(self):
#         print('Быстроходный боевой корабль с сильным артиллерийским, минным и ракетным вооружением.')
#
#
# c = Frigate(900, 55, 3500)
# print(c.get_info())
# c.advantages()
# print('--------------')
#
# a = Destroyer(5000, 61, 3800)
# print(a.get_info())
# a.advantages()
# print('--------------')
#
# b = Cruiser(1500, 53, 5300)
# print(b.get_info())
# b.advantages()



### Зад.3. Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки и т.д.). Реализовать методы для вывода суммы на экран,
# задания значений для частей.

# class Money():
#
#     def __init__(self, dollar, cent):
#         self.dollar = dollar
#         self.cent = cent
#
#
#     def __add__(self, other):
#         new_dollar = self.dollar + other.dollar
#         new_cent = self.cent + other.cent
#         new_dollar += new_cent // 100
#         new_cent = new_cent % 100
#         return new_dollar, new_cent
#
#
# a = Money(80, 30)
# b = Money(20, 75)
# print(a + b)
# a = Money(23, 43)
# b = Money(15, 25)
# print(a + b)
