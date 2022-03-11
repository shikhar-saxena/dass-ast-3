from lib2to3.pytree import type_repr
from tabnanny import check
from src.character import King
from src.grid import Village, Wall
from src.input import input_to, Get
import os


class Game:
    def __init__(self):
        """`troops` keeps track of King and all troops (alive/dead)"""

        self.village = Village()
        self.king = King(self.village)
        self.troops = []
        self.troops.append(self.king)

    def __call__(self):
        while True:
            self.king.render_health()
            self.village.render()
            ch = input_to(Get())
            self.handle_input(ch)
            os.system("clear")
            if self.check_game_victory():
                print(
                    """
__     _____ ____ _____ ___  ______   __
\ \   / /_ _/ ___|_   _/ _ \|  _ \ \ / /
 \ \ / / | | |     | || | | | |_) \ V / 
  \ V /  | | |___  | || |_| |  _ < | |  
   \_/  |___\____| |_| \___/|_| \_\|_|  
                                        

                """
                )
                return
            elif self.check_game_defeat():
                print(
                    """
 ____  _____ _____ _____    _  _____ 
|  _ \| ____|  ___| ____|  / \|_   _|
| | | |  _| | |_  |  _|   / _ \ | |  
| |_| | |___|  _| | |___ / ___ \| |  
|____/|_____|_|   |_____/_/   \_\_|  

                """
                )
                return

    def handle_input(self, ch):

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
            self.king.move_up(self.village)
        elif ch == "a" or ch == "A":
            self.king.move_left(self.village)
        elif ch == "s" or ch == "S":
            self.king.move_down(self.village)
        elif ch == "d" or ch == "D":
            self.king.move_right(self.village)

        if ch == " ":
            self.king.attack(self.village)

    def check_game_victory(self):
        for building in self.village.buildings:
            if type(building) != Wall:
                return False

        return True

    def check_game_defeat(self):
        for troop in self.troops:
            if not troop.check_death():
                return False

        return True


if __name__ == "__main__":
    Game()()
