# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

UPPER_LIMIT = 1000
LOWER_LIMIT = 0

num = randint(LOWER_LIMIT, UPPER_LIMIT)


def guess_the_number(number):
    count = 10
    while count > 0:
        choice = int(input('Введите число от 0 до 1000: '))
        if choice == number:
            print('Поздравляем! Вы угадали!')
            break
        elif choice > number:
            count -= 1
            print(f'меньше, осталось попыток : {count}')
        else:
            count -= 1
            print(f'больше, осталось попыток : {count}')
    else:
        print('К сожалению вы не угадали, можете попробовать снова')


guess_the_number(num)
