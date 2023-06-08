##READING

##lorem_text = open('sample.txt')
##for line in lorem_text:
##    if 'let' in line.lower():
##        print(line, end='')
##
##lorem_text.close()

##помешает все строки в лист и поочередно выводит.
##При больших файлах лучше не использовать
##чтобы сильно не занимать память
##with open('sample.txt', mode='r') as lorem_text:
##    for line in lorem_text.readlines():
##        print(line)


##По очереди берет каждую строку и выводит.
##после следующую строку и т.д.
##Хорошо работает при больших файлах, не использует много памяти
##with open('sample.txt', mode='r') as lorem_text:
##    line = lorem_text.readline()
##    
##    while line:
##        print(line)
##        line = lorem_text.readline()


##Читает весь файл целиком
##with open('sample.txt', mode='r') as lorem_text:
##    print(lorem_text.read())
    



##WRITING
colors_list = ['gold', 'red', 'orange', 'yellow', 'green', 'blue', 'indige', 'violet']

##Перезааписывает файл, если не существует файла с таким именем
##то создает новый и перезаписывает в него данные
##не очень безопасный способ
##w-write
##with open('rainbow_colors.txt', mode='w') as colors:
##    for color in colors_list:
##        print(color, file=colors)
##


##Добавляет данные в конец файла,Если нет файла с таким именем
##то создает и добавляет в него данные
#a-append
with open('rainbowpp.txt', mode='a') as colors:
    print('SeaGreenBLue', file=colors)



