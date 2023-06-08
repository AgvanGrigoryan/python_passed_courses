import shelve

##with shelve.open('shelve_test', ) as cars:
##    cars['opel'] = 'Germany'
##    cars['ford'] = 'USA'
##    cars['mazda'] = 'Japan'
##    cars['renault'] = 'France'
##
##    print(cars['opel'])
##    print(cars['ford'])
##    print(cars['mazda'])
##    print(cars['renault'])
##
##    del cars['renault']
##    print(cars.get('renault'))
##
##    for key in cars:
##        print(f"{key} : {cars[key]}")


##with shelve.open('shelve_test') as cars:
##    while True:
##        key = input("Get cars country with name('q' for quite): ")
##        if key == 'q':
##            break
##        country = cars.get(key, None)
##        if country is None:
##            confirm = input(f"Not Found Car with name '{key}'\nDo you want to add this car name in data base?(y-yes,something else for no): ")
##            if confirm == 'y':
##                new_car_country = input(f"Input '{key}' car Country name: ")
##                cars[key] = new_car_country
##        else:
##            print(country)


with shelve.open('shelve_test') as cars:
    temp_country = cars['niva']+',Russia'
    cars['niva'] = temp_country
##Такой метод обновления заключается в том что загрузить текущие данные в временной файл
##после добавить новые данные и  переопределить старые данные
##Здесь при использовании append мы бы не смогли бы сразу увидеть обновление
##так как данные сохраняются после with, для этого используется
##подход который показан ниже

##method append рабоатет интерактивно тогда, когда указываем аттрибут writeback=True тоесть можем сразу же после
##его использования увидеть изменённые данные но стоит учесть то,
##что данные хранятся в памяти и все равно сохраняются в файл после with
## и при больщих данные может возикнуть пробдемы


with shelve.open('shelve_test', writeback=True) as cars:
    cars['niva']
    cars['niva'].append('Vengria')
    print(cars['niva']

with shelve.open('shelve_test') as cars:
    print(cars['niva'])
    
    
