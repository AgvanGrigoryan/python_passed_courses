##__repr__() and __str__
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The Object Lion - {super().__repr__()}'

    def __str__(self):
        return f'Lion {self.name}'

##task 1
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value != 'male' and value != 'female':
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            value = 'male'
        self.__gender = value

    def __str__(self):
        appeal = 'Гражданка' if self.gender =='female' else 'Гражданин'
        return f"{appeal} {self.surname} {self.name}"

        

##task 2
class Vector:
    def __init__(self, *args):
        self.points = args

    @staticmethod
    def _quickSort(arr):
        if not arr:
            return []
        greater = []
        less = []
        base = arr.pop(0)
        for num in arr:
            if num>=base:
                greater.append(num)
            else:
                less.append(num)
        return Vector._quickSort(less) + [base] + Vector._quickSort(greater)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, values):
        integers = [value for value  in values if isinstance(value,int)]
        self.__points = self._quickSort(integers)


    def __str__(self):
        if self.points:
            return f"Vector({', '.join(map(str, self.points))})"
        else:
            return 'Empty Vector'
        
            
        
##__len__() and __abs__()
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)

class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x2 - self.x1)


##__add__() and __mul__()
##using the class Vector from the previous lesson
import math
class Vector:
    def __init__(self, *args):
        self.points = args

    @staticmethod
    def _quickSort(arr):
        if not arr:
            return []
        greater = []
        less = []
        base = arr.pop(0)
        for num in arr:
            if num>=base:
                greater.append(num)
            else:
                less.append(num)
        return Vector._quickSort(less) + [base] + Vector._quickSort(greater)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, values):
        integers = [value for value  in values if isinstance(value,int)]
        self.__points = self._quickSort(integers)


    def __str__(self):
        if self.points:
            return f"Vector({', '.join(map(str, self.points))})"
        else:
            return 'Empty Vector'

    def __len__(self):
        return len(self.points)
        
    def __add__(self, value):
        if isinstance(value, int):
            result = [point+value for point in self.points]
        elif isinstance(value, Vector):
            if len(value) == len(self):
                result = [sum(i) for i in zip(value.points, self.points)]
            else:
                raise ValueError('Addition of two vectors of different lengths is unacceptable')
        else:
            raise ValueError(f'A Vector cannot be added to a {value} {type(value)}. Expected Int or Vector(with similar length)')
        return Vector(*result)

    def __mul__(self, value):
        if isinstance(value, int):
            result = [point*value for point in self.points]
        elif isinstance(value, Vector):
            if len(value) == len(self):
                result = [math.prod(i) for i in zip(value.points,self.points)]
            else:
                raise ValueError('Multiplication of two vectors of different lengths is unacceptable')
        else:
            raise ValueError(f'A Vector cannot be multiplied to a {value} {type(value)}. Expected Int or Vector(with similar length)')
        return Vector(*result)
    
##    __sub__(-), __truediv__(/)


##Comparison magic methods
##__eq__ - ==
##__ne__ - !=
##__lt__ - <
##__le__ - <=
##__gt__ - >
##__ge__ - >=

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
        elif isinstance(other, (int, float)):
            return self.area == other

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
        
    def __gt__(self,other):
        return not self<=other

    def __ge__(self,other):
        return not self<other

    def __le__(self, other):
        return self==other or self<other

        
##task 1
class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, (int, float)):
            return self.rating == other
        else:
            raise ValueError("Comprasion is not possible")
        

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, (int, float)):
            return self.rating > other
        else:
            raise ValueError("Comprasion is not possible")

    def __lt__(self, other):
        return self!=other and not self>other


##__eq__() and __hash__()

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and \
                self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


##total ordering
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance<other.balance

        

##__bool__() if this mehod not defined will call __len__()

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __len__(self):
        print('called __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('called __bool__')
        return self.x != 0 or self.y !=0


##task 1

class City:
    def __init__(self,name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return  self.name[-1] not in ('a', 'e', 'i', 'o', 'u')

    
##task 2 
class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width

    def __str__(self):
        if self.width == self.height:
            return f"Cube size {self.width}X{self.height}"
        else:
            return f"Rectangle size {self.width}X{self.height}"


    def __bool__(self):
        return self.width == self.height


##__call__()

class Counter:
    def __init__(self):
        self.counter = 0
        self.sum = 0
        self.length = 0
        print('Init')

    def __call__(self, *args, **kwargs):
        self.counter+=1

        self.sum += sum(args)
        self.length += len(args)
        
        print(f'Our instance is called {self.counter} times')
    
    def average(self):
        return self.sum / self.length

from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Function {self.fn.__name__} is calling")
        result = self.fn(*args,**kwargs)
        finish = perf_counter()

        print(f"Function is worked at {finish-start}")
        return result


def fact(n):
    factorial = 1
    for num in range(1,n+1):
        factorial*=num

    return factorial



def fib(length: int):
    if length<=2:
        return 1
    return fib(length-1) + fib(length-2)

@Timer
def goodFib(length: int):
    a = 1
    b = 1
    
    for num in range(length-2):
        c = a+b
        a=b
        b=c
    return b


##task 1

class Addition:
    def __call__(self, *args, **kwargs):
        args_sum = sum(map(lambda x: x if isinstance(x,int) and not isinstance(x,bool) else 0,args))
        print(f"Given arguments Sum is equal {args_sum}")

##task 2
from time import time
class Timerr:
    def __init__(self, func):
        self.fn = func

    def __call__(self,*args,**kwargs):
        start = time()
        self.fn(*args,**kwargs)
        finish = time()
        return f"Function working time is {finish-start}"

    
def calculate():
    for i in range(10000000):
        2**100


##Polimophism
class Rectangle:

    def __init__(self, a ,b):
        self.a = a
        self.b = b
        
    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"



class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a**2
    
##rect1 = Rectangle(3,4)
##rect2 = Rectangle(12,5)

##print(rect1.get_rect_area(),rect2.get_rect_area())

##sq1 = Square(5)
##sq2 = Square(7)

##print(sq1.get_sq_area(),sq2.get_sq_area())


##figures = [rect1, rect2, sq1, sq2]
##
##for figure in figures:
##    print(figure)




##task 1
class UnitedKingdom:
    @staticmethod
    def capital():
        print("London is the capital of Great Britian.")

    @staticmethod
    def language():
        print("English is the primary language of Great Britain.")


class Spain:
    @staticmethod
    def capital():
        print("Madrid is the capital of Spain.")

    @staticmethod
    def language():
        print("Spanish is the primary language of Spain.")



##__getitem__(), __setitem__(), __delitem__()
class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0<=item<len(self.values):
            return self.values[item]
        else:
            raise IndexError("Index Out of our list size")

    def __setitem__(self, key, value):
        if 0<=key<len(self.values):
            self.values[key] = value
        elif key>len(self.values):
            diff = key-len(self.values)
            self.values.extend([None]*diff)
            self.values.append(value)
        else:
            raise IndexError("Index Out of our list size")

    def __delitem__(self, key):
        if 0<=key<len(self.values):
            del self.values[key]
        else:
            raise IndexError("Index Out of our list size")
        
##task 1

class Building:
    def __init__(self,floors):
        self.floors = dict(zip(range(1,floors+1),[None]*floors))
        print(self.floors, len(self.floors))

    def __setitem__(self, floor:int, company:str):
        if 1<=floor<=len(self.floors):
            self.floors[floor] = company
        else:
            raise IndexError('Building haven\'t same floor')

    def __getitem__(self, floor):
        if 1<=floor<=len(self.floors):
            return self.floors[floor]
        else:
            raise IndexError('Building haven\'t same floor')

    def __delitem__(self, floor):
        if 1<=floor<=len(self.floors):
            self.floors[floor] = None
        else:
            raise IndexError('Building haven\'t same floor')


##__iter__(), __next__()
class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('call iter')
        return iter(self.name)


##task 1 
class PowerTwo:
    def __init__(self, number:int):
        self.powTwo = number
        

    @property
    def powTwo(self):
        return self.__powTwo

    @powTwo.setter
    def powTwo(self, num:int):
        if num & (num-1) == 0:
            self.__powTwo = list()
            for i in range(1,num+1):
                if i & (i-1) == 0:
                    self.__powTwo.append(i)
        else:
            raise ValueError("This number is not power of two")

    def __iter__(self):
        self.__iteratorNum = 0 
        return iter(self.__powTwo)


    def __next__(self):
        if self.__iteratorNum >=len(self.name):
            self.__iteratorNum = 0
        nextItem = self.powTwo[self.__iteratorNum]
        self.__iteratorNum+=1
        return nextItem


##task 2
class InfinityIterator:
    def __iter__(self):
        self.__iter_index = 0
        return iter(self.__next__,2)

    def __next__(self):
        index = self.__iter_index
        self.__iter_index+=10
        return index
    
    
        


















