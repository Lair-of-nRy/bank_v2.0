def all_funds(data) -> int:
    return (5000 * data[5000]) + (2000 * data[2000]) \
           + (1000 * data[1000]) + (500 * data[500])


def is_possibility(fnd, val) -> bool:
    return fnd >= val


def replenishment() -> int:
    try:
        data = int(input('-> '))
    except ValueError:
        print('Число должно быть целым положительным')
        return replenishment()
    if data < 0:
        print('Число должно быть целым положительным')
        return replenishment()
    return data


def is_have_not_cash(data) -> bool:
    if data[5000] == 0 and data[2000] == 0 \
            and data[1000] == 0 and data[500] == 0:
        return True
    return False


def welcome():
    print('Вас приветствует БАНКнеБАНК')


def goodbye():
    print('Хорошего дня')


def choice() -> int:
    try:
        data = int(input('-> '))
    except ValueError:
        print('Неверное значение')
        return choice()
    if data != 1 and data != 2 and data != 3:
        print('Неверное значение')
        return choice()
    return data


def display_atm_balance(data):
    print("Текущий баланс банкомата:")
    print(f"5000: {data[5000]}")
    print(f"2000: {data[2000]}")
    print(f"1000: {data[1000]}")
    print(f"500: {data[500]}")
    print(f"Общая сумма: {all_funds(data)}")
