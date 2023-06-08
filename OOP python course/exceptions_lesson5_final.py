##Exceptions  in Python

##Every Errors is class in python, and theese have inheritance

##task 1
class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self,value):
        if not isinstance(value,str):
            raise TypeError('Invalid currency type')
        elif len(value)!=3:
            raise NameError('Invalid name length of currency')
        elif not value.isupper():
            raise ValueError('Currency name must be include only from Upper Letters')
        self.__currency = value

    def __eq__(self, other):
        if not isinstance(other,Wallet):
            raise TypeError(f'Wallet not supported comparing with {other}')

        if self.__currency != other.__currency:
            raise ValueError('You Can\'t compare different currencies')

        return self.balance == other.balance


    def __add__(self,other):
        if not isinstance(other, Wallet) or self.__currency != other.__currency:
            raise ValueError('This opearation is prohibited')
        return Wallet(self.__currency, self.balance+other.balance)
                            
    def __sub__(self,other):
        if not isinstance(other, Wallet) or self.__currency != other.__currency:
            raise ValueError('This opearation is prohibited')
        return Wallet(self.__currency, self.balance-other.balance)




##Распространение исключений
def first():
    print('start first')
    try:
        second()
    except:
        print('Handled')
    
    print('finish first')

def second():
    print('start second')
    1/0
    print('finish second')

##print('hello')
##first()



##Exception handling

##try:
##    a+b
##    1/0
##    int('hello')
##
##except ValueError:
##    print('Value Error handled')
##except ZeroDivisionError:
##    print('ZeroDivisionError handled')
##except NameError:
##    print('NameError handled')

##-------------

s = 'hello'
d = {}

try:
    9/0
except (KeyError, IndexError):
    print('it is Lookup error')
except ZeroDivisionError as err:
    print('ZeroDivisionError')
    print(f"Logging error {repr(err)}")
else:
    print('good')
##else code working when not have errors
finally:
    print('end')
##finally block works always after code
    


##Raise instruction
##можно возбуждать исключения в любой части кода,
##встроенные или самописаные

##try:
##    raise ValueError('oshibka znacheniya')
##except ValueError as first:
##    try:
##        raise TypeError('oshibka tipa')
##    except TypeError as second:
##        raise Exception('Bolshoye isklucheniye') from first


##from 'Error Name' указывает на то от какой
##ошибки вывеститекущую ощибку

##При добавлении фрагмента from None во время того,
##когда возбудили исключение прежние ошибки нк будут отображаться



##User custom exceptions

class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"MyException ({self.message})"
        else:
            return "MyException is empty"



raise MyException("I hate this code, and calling MyException",'fuuuu')
    


