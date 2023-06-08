##assertion - утверждения
##assert 2 + 2 ==4, '2+2 must uquals (4)four'

##def divide(a,b):
##    assert b!=0, 'B must not uquals 0'
##    return a / b


# assertions not working if program is started in optimise mode( python -O assertions.py )
def multiply_pos_nums(a, b):
    assert a > 0 and b > 0, "A,B must be positive"
    print(a * b)


multiply_pos_nums(3, -5)
