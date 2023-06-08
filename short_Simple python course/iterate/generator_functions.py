def count_up_to(x):
    count = 1
    while count<=x:
        yield count
        count +=1

print(count_up_to(4))
counter = count_up_to(4)
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())


##Generator expretion
counter2 = (number for number in range(10))

print(counter2)
