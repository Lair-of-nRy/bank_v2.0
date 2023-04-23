from tools import *
from utils import *
from decorators import *

DATA = {5000: 0, 2000: 0, 1000: 0, 500: 0}

welcome()


@dec_choice
def choice_input():
    return choice()


def main():
    while True:
        c = choice_input()
        if c == 1:
            choice_1(DATA)
        elif c == 2:
            atm_replenishment(DATA)
        else:
            goodbye()
            break


main()
