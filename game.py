from src.character import Balloon, King, Queen, Barbarian, Archer
from src.grid import Village, Wall, Cannon, WizardTower
from src.input import input_to, Get
import os


class Game:
    def __init__(self):
        """`troops` keeps track of King and all troops (alive/dead)"""

        self.village = Village()

        print("Choose Character")

        print(
            """
█▀▀ █░█ █▀█ █▀█ █▀ █▀▀   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
█▄▄ █▀█ █▄█ █▄█ ▄█ ██▄   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
"""
        )

        print()
        print(
            """
█▀█ ▀   █▄▀ █ █▄░█ █▀▀
█▄█ ▄   █░█ █ █░▀█ █▄█
        """
        )
        print()
        print(
            """
▄█ ▀   █▀█ █░█ █▀▀ █▀▀ █▄░█
░█ ▄   ▀▀█ █▄█ ██▄ ██▄ █░▀█
        """
        )

        while True:
            ch = input_to(Get())

            if not ch:
                continue

            if ch == "0":
                self.playable_character = King(self.village)
                break
            elif ch == "1":
                self.playable_character = Queen(self.village)
                break

        self.troops = []
        self.troops.append(self.playable_character)
        self.choice = ch

    # Not destroyed cannons attack the troops
    def cannon_attack(self):

        for building in self.village.buildings:
            if type(building) == Cannon:
                building.attack(self.troops)

    # Not destroyed wizards attack the troops
    def wizard_attack(self):

        for building in self.village.buildings:
            if type(building) == WizardTower:
                building.attack(self.troops)

    # Move Troops (barbarians)
    def move_troops(self):
        for troop in self.troops:
            if type(troop) == King or type(troop) == Queen:
                continue
            troop.move(self.village)

    def count_troop(self, troop_type):
        count = 0
        for troop in self.troops:
            if type(troop) == troop_type:
                count += 1
        return count

    def reset_attacks_troops(self):
        """Increment counter (no of attacks) for the troops present (after each timestamp)"""
        for troop in self.troops:
            if type(troop) == King or type(troop) == Queen:
                continue
            troop.reset_counter()

    def __call__(self):
        while True:
            self.playable_character.render_health()
            self.village.render(self.troops)
            ch = input_to(Get())
            self.handle_input(ch)
            self.move_troops()
            self.cannon_attack()
            self.wizard_attack()
            os.system("clear")
            self.reset_attacks_troops()
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
            self.playable_character.move_up(self.village)
        elif ch == "a" or ch == "A":
            self.playable_character.move_left(self.village)
        elif ch == "s" or ch == "S":
            self.playable_character.move_down(self.village)
        elif ch == "d" or ch == "D":
            self.playable_character.move_right(self.village)
        elif ch == "1" or ch == "2" or ch == "3":
            barbarian = self.village.spawn_pts[ord(ch) - 49].add_troop(
                self.village, self, Barbarian
            )

            if barbarian is not None:
                self.troops.append(barbarian)
        elif ch == "4" or ch == "5" or ch == "6":
            archer = self.village.spawn_pts[ord(ch) - 52].add_troop(
                self.village, self, Archer
            )

            if archer is not None:
                self.troops.append(archer)
        elif ch == "7" or ch == "8" or ch == "9":
            balloon = self.village.spawn_pts[ord(ch) - 55].add_troop(
                self.village, self, Balloon
            )

            if balloon is not None:
                self.troops.append(balloon)
        elif ch == " ":
            self.playable_character.attack(self.village)
        elif (ch == "l" or ch == "L") and self.choice == "0":
            self.playable_character.leviathan_axe(self.village)
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
