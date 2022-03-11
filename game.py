from lib2to3.pytree import type_repr
from src.character import King
from src.grid import Village
from src.input import input_to, Get
import os

# import os


# def spawn():
#     pass


def handle_input(ch, king, village):

    # if(ch == 1 or ch == 2 or ch == 3): TODO:

    # switch = {
    #     # 1: spawn(),
    #     # 2: spawn(),
    #     # 3: spawn(),
    #     # # Add Spells
    #     "w": "move_up",
    #     "W": "move_up",
    #     "a": "move_left",
    #     "A": "move_left",
    #     "s": "move_down",
    #     "S": "move_down",
    #     "d": "move_right",
    #     "D": "move_right",
    # }

    # func_name = switch[ch]

    # king.func_name(village)
    # king.func_name(village)

    if ch == "w" or ch == "W":
        king.move_up(village)
    elif ch == "a" or ch == "A":
        king.move_left(village)
    elif ch == "s" or ch == "S":
        king.move_down(village)
    elif ch == "d" or ch == "D":
        king.move_right(village)

    if ch == " ":
        king.attack(village)


def main():

    village = Village()
    king = King(village)

    while True:
        village.render()
        ch = input_to(Get())
        handle_input(ch, king, village)
        os.system("clear")


if __name__ == "__main__":
    main()
