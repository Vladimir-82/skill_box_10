# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
import random
def one_day():
    dice = random.randint(1, 13)
    if dice == 8:
        raise IamGodError('Сегодня я бог!')
    elif dice == 9:
        raise DrunkError('Сегодня я напился!')
    elif dice == 10:
        raise CarCrashError('Сегодня я попал в автокатастрофу!')
    elif dice == 11:
        raise GluttonyError('Сегодня я обожрался!')
    elif dice == 12:
        raise DepressionError('Сегодня я плачу!')
    elif dice == 13:
        raise SuicideError('Сегодня я стреляю в голову!')
    else:
        return dice

carma_file = 'carma.txt'
file = open(carma_file, mode='w', encoding='utf8')
day = 1
total_carma = 0
while True:
    file.write(f'\n ******День - {day}******')
    try:
        total_carma += one_day()
    except IamGodError as God:
        file.write(f'\n Бог {God}')
    except DrunkError as Drunk:
        file.write(f'\n Напился {Drunk}')
    except CarCrash as Car:
        file.write(f'\n Я Шумахер {Car}')
    except GluttonyError as Glut:
        file.write(f'\n Пережрал {Glut}')
    except DepressionError as Depress:
        file.write(f'\n Депрессия {Depress}')
    except SuicideError as Suicide:
        file.write(f'\n Я депрессирую {Suicide}')
    file.write(f'\n Карвма просветления составляет: {total_carma}')
    # print(total_carma)
    day += 1
    if total_carma >= ENLIGHTENMENT_CARMA_LEVEL:
        file.write(f'\n Вы освободились от кармы за {day - 1} дней!')
        break


# https://goo.gl/JnsDqu
