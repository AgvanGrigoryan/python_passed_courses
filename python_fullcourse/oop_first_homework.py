import math
##task 1
class Line:
    def __init__(self, cord1: tuple, cord2: tuple):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self) -> float:
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2 - y1)/(x2 - x1)
        
##task 2

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return round(math.pi*self.radius**2*self.height,2)

    def surface_area(self):
        r = self.height
        h = self.radius
        return round(2*math.pi*r*h+(math.pi*r**2)*2,1)


##task 3

class Account:
    def __init__(self, name, balance=0):
        self.owner = name
        self.balance = balance

    def __str__(self):
        return f'Владелец счёта: {self.owner} \nБаланс счёта: ${self.balance}'

    def deposit(self, amount):
        if not isinstance(amount, int):
            print('Введите число!')
        else:
            self.balance+=amount
            return 'Внесение выполнено'

    def withdraw(self, amount):
        if not isinstance(amount, int):
            print('Введите число!')
        elif amount > self.balance:
            print('Введенная сумма больше текущего баланса')
        else:
            self.balance-=amount
            return 'Снятие выполнено'
        
