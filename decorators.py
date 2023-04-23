

def dec_choise(func):
    def wrapper():
        print('какое действие хотите выполнить?\n\
            1 - снятие наличных     2 - инкассация\
            3 - выход')
        choise = func()
        return choise
    return wrapper
    
