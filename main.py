from engine import comp_number, input_number, check, game_over

print("Игра Быки и Коровы. Компьютер загадывает 4-х значное положительное число, цифры которого НЕ повторяются.")

pc_number = comp_number()

while True:
    number_user = input_number()
    result = check(number_user)

    if game_over(result):
        break

    for i in result:
        print(i, result[i])

print('Ты победил! Это было - ', pc_number)
