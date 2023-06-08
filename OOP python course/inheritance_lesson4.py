##Inheritance introduction
class Person:# parent
    def can_breathe(self):
        print('I can breath')

    def can_walk(self):
        print('I can walk')

class Doctor(Person): #subclass
    def can_cure(self):
        print('I can Cure')

class Architect(Person):#subclass
    def can_build(self):
        print('I can build a building')


## task 1

class Vehicle:
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

class Car(Vehicle):
    pass

class RaceCar(Car):
    pass


##inheritance from object
##by default every classes is subclass of object
class Mylist(list):
    pass

##task 1
import math
class NewInt(int):
    def repeat(self,k:int=2):
        if k>0:
            return int(str(self)*k)
        else:
            print('Input only a Positive number')

    def to_bin(self):
        return int(bin(self)[2:])

    
##Overriding
##Переопределение методов, сначала ищется в экземпляре модели
##...

##  Extending
    
class Person:
    pass

class Doctor(Person):
    def sleep(self):
        print('Doctor speeps')

##p = Person()
##d = Doctor()


##Delegating
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def breathe(self):
        print('Person Breathes')

class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name,surname)
        self.age = age
        
    def breathe(self):
        print('Doctor Breathes')
        super().breathe()


##task 1

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Transport type {self.kind} of brand {self.brand} can be accelerateed to {self.max_speed} km/h"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand,max_speed, 'Car')
        self.mileage = mileage
        self._gasoline_residue = 0
        self.gasoline = gasoline_residue

    @property
    def gasoline(self):
        return self._gasoline_residue

    @gasoline.setter
    def gasoline(self, value:int):
        if not isinstance(value,int):
            print("Car Fuel increass error")
        elif value>=0:
            self._gasoline_residue+=value
            print(f"Fuel volume is increased by {value} liters and is {self._gasoline_residue}liters")
        else:
            print("Don\'t steal fuel🧐")


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name:str):
        super().__init__(brand,max_speed, 'Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f"{self.owners_name} owns the boat of brand {self.brand}"

class Plane(Transport):
    def __init__(self,brand, max_speed, capacity):
        super().__init__(brand,max_speed, 'Plane')
        self.capacity = capacity

    def __str__(self):
        return f"The plane of brand {self.brand} includes {self.capacity} peoples"
    



##task2

class Initialization:
    def __init__(self, capacity, food):
        if isinstance(capacity, int) and not isinstance(capacity, bool):
            self.capacity = capacity
            self.food = food
        else:
            print("Количество людей должно быть целым числом")

    @property
    def food(self):
        return self._food
        
    @food.setter
    def food(self, value):
        if isinstance(value,(list, tuple)):
            self._food = value
        else:
            print("Укажите food списком")


class Vegetarian(Initialization):
    def __init__(self,capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо!Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity,food)


    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Из самая любимая еда {self.food}"
    
    def __eq__(self, other):
        if isinstance(other, Initialization):
            return self.capacity==other.capacity
        elif isinstance(other,int) and not isinstance(other,bool):
            return self.capacity == other
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"
        

    def __lt__(self, other):
        if isinstance(other, Initialization):
            return self.capacity < other.capacity
        elif isinstance(other,int) and not isinstance(other,bool):
            return self.capacity < other
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"
          

    def __gt__(self, other):
        if isinstance(other, Initialization):
            return self.capacity > other.capacity
        elif isinstance(other, int) and not isinstance(other, bool):
            return self.capacity > other
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"


##Множественное наследование

class Doctor:
    def __init__(self, degree):
        self.degree = degree
    
    def can_cure(self):
        print('I am a Doctor, I can cure')

    def graduate(self):
        print('Ура я отучился на доктора')

class Builder:
    def __init__(self,rank):
        self.rank = rank
        
    def can_build(self):
        print('I am a Builder, i can build')

    def graduate(self):
        print('Ура я отучился на строителя')


class Person(Doctor, Builder):
    def __init__(self, degree, rank):
        super().__init__(degree)
        Builder.__init__(self,rank)
    
    def can_breathe(self):
        print('I am a Person, I can breathes')

    def can_build(self):
        print('I am a Person, and I am also can build')

    def __str__(self):
        print(f'Person {self.rank} {self.degree}')

##Если дочерний класс имеет метод с одинаковым именем
##как у родителя то как и всегда ищется сначала
##в дочернем классе потом в родительских,
##следовательно сработает метод дочернего класса

##сначала ищется метод или аттрибут в самом экземляре класса,
##если не назодит то по порадку наследование
##проходится по родителям и ищет метод или аттрибут

        
## с помощью метода instance_name.__mro__
##можем проверить порядок поиска методов



##MRO - Method Resolution order
##class A:
##    pass
##
##class B:
##    def hello(self):
##        print('hello from B')
##
##class C(A,B):
##    pass
##
##class D:
##    def hello(self):
##        print('hello from D')
##
##class E:
##    def hello(self):
##        print('hello from E')
##
##class F(D,E):
##    def hello(self):
##        print('hello from F')
##
##class G(C,F):
##    pass

class O: pass
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass

class K1(C,A,B): pass
class K2(A,D): pass
class K3(B,D,E): pass

class Z(K1,K2,K3): pass

##print(Z.mro())


##Slots
##Преимущество и плюсы Слотов
##1. Ограничивает аттрибуты, опперации добавления новых,
##ненужных аргументов и методов в класс

##2.Занимает Меньше памяти из-за того что у класса
##нет словаря __dict__ который занимает
##допольнительное место в памяти

##3.Работает быстрее чем обычный класс 


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3,4)
ps = PointSlots(3,4)

##Проверка на память
##print(f'Point class without __slots__ Sizeof - {p.__sizeof__()}, __dict__ size {p.__dict__.__sizeof__()}')

##У Класса с слотами нет словаря __dict__
##print(f'PointSlots class with __slots__ Sizeof - {ps.__sizeof__()}, __slots__ size {ps.__slots__.__sizeof__()}')


from timeit import timeit
def Class_without_slots_speed():
    c = Point(6,7)
    c.x = 900
    c.y = 2
    c.y
    c.x
    del c.x
    del c.y

def Class_with_slots_speed():
    c = PointSlots(6,7)
    c.x = 900
    c.y = 2
    c.y
    c.x
    del c.x
    del c.y

##Проверка на скорость
##print("Class without slots speed - ",timeit(Class_without_slots_speed))
##print("Class with slots speed - ",timeit(Class_with_slots_speed))


##Working at Slots with property and inheritance

class Rectangle:
    __slots__ = ('__width', 'height')

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value
        
    @property
    def area(self):
        return self.width*self.height




class Square(Rectangle):
    __slots__ = 'color'

    def __init__(self, a, color):
        super().__init__(a,a)
        self.color = color







