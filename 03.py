# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass

def varification(line):
    name, mail, age = line.split(' ')
    if not name.isalpha():
        raise NotNameError('поле имени содержит НЕ только буквы')
    if 10 >= int(age) or int(age) >= 99:
        raise BaseException('поле возраст НЕ является числом от 10 до 99')

    if '.' not in line or '@' not in line:
        raise NotEmailError('поле емейл НЕ содержит @ и .')

good_file = open('registrations_good.log', mode='w', encoding='utf8')
bad_file = open('registrations_bad.log', mode='w', encoding='utf8')
with open('registrations.txt', mode='r', encoding='utf8') as file:
    for line in file:
        line = line[:-1:]
        try:
            varification(line)
            good_file.write(line)
            good_file.write('\n')

        except ValueError as val:
            bad_file.write(f'{line} НЕ присутсвуют все три поля или перепутаны поля {line} {val} \n')
        except NotNameError as name_error:
            bad_file.write(f'{line} {name_error} \n')
        except BaseException as age:
            bad_file.write(f'{line} {age} \n')
        except NotEmailError as mail_error:
            print(f'{line} {mail_error} \n')
            bad_file.write(f'{line} {mail_error} \n')


good_file.close()
bad_file.close()