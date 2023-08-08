##lambda functions
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
map(square,my_nums)
##for item in map(square,my_nums):
##    print(item)

square_nums = list(map(square,my_nums))
##print(square_nums)

def splicer(mystring):
    if len(mystring) %2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally', 'Agvan']
##print(list(map(splicer, names)))
    

def check_even(num):
    return num%2==0

mynums = [1,2,3,4,5,6]
##print(list(filter(check_even, mynums)))

##print(list(map(lambda num: num**2,mynums)))


print(list(filter(lambda x: x%2==0, mynums)))

print(list(map(lambda name: name[:5], names)))













