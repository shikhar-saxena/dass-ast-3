from src.character import King
from src.grid import Village, Wall, Cannon
from src.input import input_to, Get
import os


class Game:
    def __init__(self):
        """`troops` keeps track of King and all troops (alive/dead)"""

        self.village = Village()
        self.king = King(self.village)
        self.troops = []
        self.troops.append(self.king)

    # Not destroyed cannons attack the troops
    def cannon_attack(self):

        for building in self.village.buildings:
            if type(building) == Cannon:
                building.attack(self.troops)

    # Move Troops (barbarians)
    def move_troops(self):
        for troop in self.troops:
            if type(troop) == King:
                continue
            troop.move(self.village)

    def __call__(self):
        while True:
            self.king.render_health()
            self.village.render(self.troops)
            ch = input_to(Get())
            self.handle_input(ch)
            self.move_troops()
            self.cannon_attack()
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

        if ch is None:
            return
        if ch == "w" or ch == "W":
            if self.king.check_death():
                return
            self.king.move_up(self.village)
        elif ch == "a" or ch == "A":
            if self.king.check_death():
                return
            self.king.move_left(self.village)
        elif ch == "s" or ch == "S":
            if self.king.check_death():
                return
            self.king.move_down(self.village)
        elif ch == "d" or ch == "D":
            if self.king.check_death():
                return
            self.king.move_right(self.village)
        elif ch == "1" or ch == "2" or ch == "3":
            barbarian = self.village.spawn_pts[ord(ch) - 49].add_troop(self.village)

            if barbarian is not None:
                self.troops.append(barbarian)
        elif ch == " ":
            self.king.attack(self.village)
        elif ch == "l" or ch == "L":
            self.king.leviathan_axe(self.village)
        else:
            return

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
