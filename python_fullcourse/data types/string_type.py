##string methods


##string format
print('Hello {}'.format('Agvan'))
print('Hello {} {} nice to meet you'.format('Agvan', 'Grigoryan'))

##Named Placeholders
print('Hello {fn} {ln}'.format(ln='Babajanyan', fn='Gevorg'))

data = {'first': 'Happy', 'last': 'Delicious'}
print('{first} {last}'.format(**data))

person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))

data = [4, 8, 15, 16, 23, 42]
print('{p[3]} {p[5]}'.format(p=data))

##padding and aligning strings
print('{:10}'.format('Agvan'))
print('{:.>10}'.format('Agvan'))

##center align
print('{:^10}'.format('Agvan'))

##Placeholder explicit positional index(in python 2.6 even mandatory)
print('{1} {0}'.format('two', 'one'))

##Value Conversion
##If you just want to render the output of str(...) or repr(...)
##you can use the !s or !r conversion flags.

class Data(object):

    def __str__(self):
        return 'converted to str'

    def __repr__(self):
        return 'converted for repr'
    
print('{0!s} {0!r}'.format(Data()))


##Truncating long strings

print('{:.3}'.format('Agvan'))

##Combining truncate and padding
print('{:_<10.3}'.format('Agvan'))




##Numbers formating
##Integers
print('{:d}'.format(42))


##Floats
print('{:f}'.format(3.141592653589793))

##Padding numbers
print('{:4d}'.format(12))

##Float truncate and precision '{value:width.precisionf}'
num = 100/777
print('Result: {n:09.2f}'.format(n=num))

##For integer values providing a precision doesn't make much sense and
##is actually forbidden in the new style (it will result in a ValueError).

print('{:04d}'.format(12))


##Signed numbers
##By default only negative numbers are prefixed with a sign.
##This can be changed of course.
print('{:+d}'.format(36))
print('{:+d}'.format(-36))

##Use a space character to indicate that negative numbers should be prefixed with a minus symbol
##and a leading space should be used for positivees ones.
print('{: d}'.format(37))
print('{: d}'.format(-37))
      
##New style formatting is also able to control the position
##of the sign symbol relative to the padding.
print('{:=5d}'.format(-41))
print('{:=+5d}'.format(41))

print(f'F string example {num}')


##DATETIME
print('===DATETIME===')
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001,2,3,4,5)))


##Parametrized formats
print('===Parametrized formats===')
print('{:{align}{width}}'.format('test', align='^', width='10'))




##Custom objects
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

print('{:open-the-pod-bay-doors}'.format(HAL9000()))


