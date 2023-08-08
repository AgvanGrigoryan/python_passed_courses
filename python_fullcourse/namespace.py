##lambda num: num**2
##global
name = 'It is Global string'

def greet():
    ##enclosing 
    name = 'Vlad'

    def hello():
        ##local
        name = 'Agvan'
        print('Hello, ' + name)

    hello()

greet()


def edit_global():
    global name
    name='New Global Name'
    print('function print ' + name)


print(name)
edit_global()
print(name)


 




