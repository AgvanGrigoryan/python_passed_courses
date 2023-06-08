
##with open('test_binary.txt', 'bw') as test_file:
##    test_file.write(bytes(range(21)))
##
##with open('test_binary.txt', 'br') as binary:
##    for line in binary:
##        print(line)


import pickle

honda = (
    'civic',
    'grey',
    '2009',
    (
        (1,'james Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green')
        
    )
)

with open('honda', 'wb') as honda_file:
    pickle.dump(honda, honda_file)

with open('honda', 'rb') as read_honda:
    honda_from_file = pickle.load(read_honda)

print(honda_from_file)
