def dec_choice(func):
    def wrapper():
        print('Какое действие хотите выполнить?\n\
            1 - снятие наличных     2 - инкассация\
            3 - выход')
        choice = func()
        return choice
    return wrapper
