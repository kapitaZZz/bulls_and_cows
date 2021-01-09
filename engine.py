import random

number_pc = None


def comp_number():
    '''
    Функция загадывает целое 4-х значное число, цифры которого не повторяются
    и не начинается с 0
    '''
    global number_pc
    digits = [x for x in range(10)]
    random.shuffle(digits)
    number_pc = digits[:4]
    if number_pc[0] == 0:
        number_pc[0] = number_pc[1]
        number_pc[1] = 0
    return number_pc


def input_number():
    '''
    Функция принимает число от пользователя и проверяет его на выполнение условий
    '''
    while True:
        number_user = input('Введите 4-х значное, положительное число, первая цифра не должна быть 0! : ')
        if len(number_user) != 4 or not number_user.isdigit():
            continue
        number_user = list(map(int, number_user))
        if len(set(number_user)) == 4:
            break
    return number_user


def check(number_user):
    '''
    Функция сравнивает цифры числа пользователя и компьютера. Выдает результат по совпадениям цифр в числах
    '''
    result = {'Быки': 0,
              'Коровы': 0}
    for i, num in enumerate(number_user):
        if num == number_pc[i]:  # вот так вот
            result['Быки'] += 1
        elif num in number_pc:
            result['Коровы'] += 1
    return result


def game_over(result):
    '''
    Завершение игры, если число полностью было угадано
    '''
    if result['Быки'] == 4:
        return number_pc
