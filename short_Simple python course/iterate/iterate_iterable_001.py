##iterable- итерируемый, те обьекты элементы которых
##можно перебирать list, tuple, dict, str

number_list = [1,2,3,4,5]

for number in number_list:
    print(number)

for letter in 'my_string':
    print(letter)

##Iterators
number_list_iter = iter(number_list)
print(type(number_list_iter))

print(number_list_iter.__next__())
print(number_list_iter.__next__())
print(number_list_iter.__next__())


string_iter = iter('my_string_iter')
print(type(string_iter))

print(string_iter.__next__())
print(string_iter.__next__())

print(next(string_iter))
print(next(string_iter))

def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            break

    

my_for_loop('Hello')
