from utils import *
# val -> значение / кол-во необходимых купюр
def calculation(val, data) -> dict:
    if val % 500 != 0:
        return 'не могу выдать сумму не кратную 500'
    else:
        n_5000 = val // 5000 
        if n_5000 <= data[5000]:
            val = val % 5000
        else:
            n_5000 = data[5000]
            val = val - (5000 * n_5000)    
        n_2000 = val // 2000
        if n_2000 <= data[2000]:
            val = val % 2000
        else:
            n_2000 = data[2000]
            val = val - (2000 * n_2000)
        n_1000 = val // 1000
        if n_1000 <= data[1000]:
            val = val % 1000
        else:
            n_1000 = data[1000]
            val = val - (1000 * n_1000)
        n_500 = val // 500
        if n_500 > data[500]:
            return 'не хватает банкнот'
        data[5000] = data[5000] - n_5000
        data[2000] = data[2000] - n_2000
        data[1000] = data[1000] - n_1000
        data[500] = data[500] - n_500
        return {'5000':n_5000, '2000':n_2000, '1000':n_1000, '500':n_500}

# инкассация
def ATM_replenishment(data):   
    print('кол-во купюр номеналом в 5000')
    data[5000] = replenishment()
    print('кол-во купюр номеналом в 2000')
    data[2000] = replenishment()
    print('кол-во купюр номеналом в 1000')
    data[1000] = replenishment()    
    print('кол-во купюр номеналом в 500')
    data[500] = replenishment()
    print('инкассация проведена')

# выбор 1 - снятие денег
def choise_1(DATA):
    not_cash = is_have_not_cash(DATA)
    if not_cash is True:
        print('в банкомате нет денег\n\
              необходимо провести инкассацию')
        return main()
    af = all_funds(DATA)
    print('желаеммая сумма')
    cv = replenishment()
    pos = is_possibility(af, cv)
    if pos is False:
        print(f'нет столько средств,\
               попробуйте сумму не больше {af}')
        return main()
    print(calculation(cv, DATA))

# основная программа
def main():
    while True:
        c = dec_choise(choise)()
        if c == 1:
            choise_1(DATA)
        elif c == 2:
            ATM_replenishment(DATA)
        else:
            goodbye()
            break