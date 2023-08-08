##def create_cubes(n):
##    for x in range(n):
##        yield x**3
##
##
##print(create_cubes(10))
##for x in create_cubes(10):
##    print(x)
##
##
##def gen_fibon(n):
##    a = 1
##    b = 1
##    for i in range(n):
##        yield a
##        a,b = b,a+b
##
##for num in gen_fibon(10):
##    print(num)
##
##
##
##def simple_gen():
##    for i in range(3):
##        yield i
##
##
##for number in simple_gen():
##    print(number)
##
##
##gen = simple_gen()
##
##
##s = 'hello'
##for letter in s:
##    print(letter)
##
##s_iter = iter(s)
##print(next(s_iter))



##task 1

print('task 1')
def genquares(n):
    for i in range(n):
        yield i**2

for num in genquares(10):
    print(num)


print('task2')
from random import randint
def rnd_num(low, high, n):
    for i in range(n):
        yield randint(low,high)

for num in rnd_num(1,10,5):
    print(num)

print('task 3')
s = 'privet'
iter_s = iter(s)
print(next(iter_s),'printed with next function')
for letter in iter_s:
    print(letter)


print('task 4')




