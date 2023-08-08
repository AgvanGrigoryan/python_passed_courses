from colorama import init, Fore, Style, Back, Cursor
init()

##task 1
for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print(Fore.RED + 'Not supported' + Fore.YELLOW + ' ** or pow operand on str type' )


##task 2

x = 5
y = 0
 
try:
    z = x/y
except ZeroDivisionError:
    print(f'{Fore.WHITE}{Back.RED}NELIZA NELIZE ARA NA NOL DELIT{Style.RESET_ALL}')
finally:
    print('Vsyo Sdelano Brat')

##task 3
while True:
    try:
        square = int(input('INPUT NUMBER, nothing else!'))
    except ValueError:
        print('Error! Try again!')
    else:
        break

print(f'Thank youu! Square number: {square**2}')
        
