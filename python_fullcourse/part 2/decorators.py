##def func():
##    return 1
##
##def hello():
##    return 'Privet'
##
##greet = hello
##
##print(greet())
##del hello
####print(hello()) # hello is not defined
##print(greet())



def hello(name='Vlad'):
    print('We are started hello function')

    def greet():
        return '\t This is greet function in hello'

    def welcome():
        return '\t this it welcome functin in hello'
    
    
    print(greet())
    print(welcome())
    print('This is function welcome')

    print('We are going to return function')

    if name == 'Vlad':
        return greet
    else:
        return welcome

new_func = hello('Vladdd')
print(new_func())




##example 2
def cool():
    def super_cool():
        return 'Super cool'

    return super_cool

some_func = cool()

print(some_func())





##example 3 give function as function attribute

def hello():
    return 'Hello Vlad'

def other(some_func):
    print('Here completing another code')
    print(some_func())


other(hello)

def new_decorator(original_func):
    def wrap_func():
        print('Some code, completed before function original_func')
        original_func()
        print('Some code, completed after function original_func')

    return wrap_func

def func_needs_decorator():
    print('This function needs at decorators')

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()


@new_decorator
def func_needs_decorator():
    print('This function needs at decorators')

print('\n\n')     
func_needs_decorator()



