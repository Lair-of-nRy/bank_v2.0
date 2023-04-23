
# n -> номинал / общая сумма всех средств 
def all_funds(data) -> int:
    return (5000 * data[5000]) + (2000 * data[2000])\
          + (1000 * data[1000]) + (500 * data[500])
     
# fnd -> средства val -> значение / проверка хватает ли средств
def is_possibility(fnd, val) -> bool:
    return fnd >= val

    
# ввод кол-ва купюр или нужной суммы
def replenishment() -> int:
    try:
        data = int(input('-> '))
    except ValueError:
        print('число должно быть целым положительным')
        return replenishment()
    if data < 0:
        print('число должно быть целым положительным')
        return replenishment()
    return data

# проверка пустой банкомат или нет
def is_have_not_cash(data) -> bool:
    if  data[5000] == 0 and data[2000] == 0\
        and data[1000] == 0 and data[500] == 0:
        return True
    return False

# приветствие
def welcome():
    print('Вас приветствует БАНКнеБАНК')

# прощание
def goodbye():
    print('хорошего дня')

# выбор действия
def choise() -> int:
    try:
        data = int(input('-> '))
    except ValueError:
        print('не верное значение')
        return choise()
    if data != 1 and data != 2 and data != 3:
        print('не верное значение')
        return choise()
    return data
