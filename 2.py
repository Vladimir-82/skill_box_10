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


class IamGodError(Exception):
    def __init__(self, messange):# переопределим параметр исключения в созданном исключении
        self.messange = 'А может, лучше черт?'
    def __str__(self):
        return self.messange

class DrunkError(Exception): # подтягивает из параметра в созданном исключении
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    dice = random.randint(1, 13)
    if dice == 8:
        raise IamGodError('Сегодня я бог!')
    elif dice == 9:
        raise DrunkError('Сегодня я напился!')
    elif dice == 10:
        raise CarCrashError('Сегодня я Шумахер!')
    elif dice == 11:
        raise GluttonyError('Сегодня я кушаю!')
    elif dice == 12:
        raise DepressionError('Сегодня я в депрессии!')
    elif dice == 13:
        raise SuicideError('Сегодня я стреляю себе в голову!')
    else:
        file.write(f'\n Я очищаюсь!!!')
        return dice

carma_file = 'carma.txt'
with open(carma_file, mode='w', encoding='utf8') as file:
    day = 1
    total_carma = 0
    while True:
        file.write(f'\n ******День - {day}******')
        try:
            total_carma += one_day()
        except IamGodError as god:
            file.write(f'\n {god}')
        except DrunkError as drunk:
            file.write(f'\n {drunk}')
        except CarCrashError as car:
            file.write(f'\n {car}')
        except GluttonyError as glut:
            file.write(f'\n {glut}')
        except DepressionError as depress:
            file.write(f'\n {depress}')
        except SuicideError as suic:
            file.write(f'\n {suic}')
        file.write(f'\n Карма просветления составляет: {total_carma}\n')
        day += 1
        if total_carma >= ENLIGHTENMENT_CARMA_LEVEL:
            file.write(f'\n Вы освободились от кармы за {day - 1} дней!')
            break


# https://goo.gl/JnsDqu
