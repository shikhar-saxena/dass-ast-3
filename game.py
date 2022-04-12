from time import sleep
from src.character import Balloon, King, Queen, Barbarian, Archer
from src.grid import Village, Wall, Cannon, WizardTower
from src.input import input_to, Get
import os


class Game:
    def __init__(self):
        """`troops` keeps track of King, Queen and all troops (alive/dead)"""
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

            if ch == "0" or ch == "1":
                self.choice = ch
                return

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

    def level(self, level_no):

        self.village = Village(level_no)

        if self.choice == "0":
            self.playable_character = King(self.village)
        else:
            self.playable_character = Queen(self.village)

        self.troops = []
        self.troops.append(self.playable_character)

        self.rage_flag = True
        self.heal_flag = True

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
                exit(0)

    def __call__(self):
        print(
            """
 _                    _   __  
| |                  | | /  | 
| |     _____   _____| | `| | 
| |    / _ \ \ / / _ \ |  | | 
| |___|  __/\ V /  __/ | _| |_
\_____/\___| \_/ \___|_| \___/
                              
                """
        )
        sleep(0.8)

        self.level(1)

        print()
        print(
            """
 _                    _   _____ 
| |                  | | / __  \
| |     _____   _____| | `' / /'
| |    / _ \ \ / / _ \ |   / /  
| |___|  __/\ V /  __/ | ./ /___
\_____/\___| \_/ \___|_| \_____/                                

                """
        )

        sleep(0.8)

        self.level(2)

        print()

        print(
            """
 _                    _   _____ 
| |                  | | |____ |
| |     _____   _____| |     / /
| |    / _ \ \ / / _ \ |     \ \
| |___|  __/\ V /  __/ | .___/ /
\_____/\___| \_/ \___|_| \____/ 
                                
                """
        )

        sleep(0.8)

        self.level(3)

        print(
            """
__     _____ ____ _____ ___  ______   __
\ \   / /_ _/ ___|_   _/ _ \|  _ \ \ / /
 \ \ / / | | |     | || | | | |_) \ V / 
  \ V /  | | |___  | || |_| |  _ < | |  
   \_/  |___\____| |_| \___/|_| \_\|_|  
                                        

                """
        )

    def handle_input(self, ch):

        if ch is None:
            return
        if ch == "w" or ch == "W":
            for _ in range(self.playable_character.movement_speed):
                self.playable_character.move_up(self.village)
        elif ch == "a" or ch == "A":
            for _ in range(self.playable_character.movement_speed):
                self.playable_character.move_left(self.village)
        elif ch == "s" or ch == "S":
            for _ in range(self.playable_character.movement_speed):
                self.playable_character.move_down(self.village)
        elif ch == "d" or ch == "D":
            for _ in range(self.playable_character.movement_speed):
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
        elif ch == "r" or ch == "R":
            if self.rage_flag:
                self.rage_spell()
        elif ch == "h" or ch == "H":
            if self.heal_flag:
                self.heal_spell()
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

    def rage_spell(self):
        for troop in self.troops:
            if not troop.check_death():
                if troop.damage * 2 < 100:  # cannot oneshot anything
                    troop.damage *= 2
                    troop.movement_speed *= 2

        self.rage_flag = False

    def heal_spell(self):
        for troop in self.troops:
            if not troop.check_death():

                max_health = 100

                if type(troop) == Archer:
                    max_health = 50

                new_health = int(troop.health * 1.50)

                if new_health > max_health:
                    troop.health = max_health
                else:
                    troop.health = new_health

        self.heal_flag = False


if __name__ == "__main__":
    Game()()
