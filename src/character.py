from colorama import Fore, Back, Style


class Character:
    def __init__(self, damage, display_character):
        self.damage = damage
        self.health = 100
        self.display_character = display_character
        self.last_moved_direction = "D"  # By default

    def init_position(self, position_n, position_m):
        self.position_n = position_n
        self.position_m = position_m

    def place_character(self, village):
        # self.temp = village.grid[self.position_n, self.position_m]
        village.grid[self.position_n, self.position_m] = self.display_character

    def clear_character(self, village):

        village.grid[self.position_n, self.position_m] = " "

    # def move(self, village):
    #     pass

    def move_up(self, village):

        if self.check_death():
            return

        up = self.position_n - 1

        if up >= 0 and village.grid[up, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = up
            self.place_character(village)

        self.last_moved_direction = "W"

    def move_left(self, village):

        if self.check_death():
            return

        left = self.position_m - 1

        if left >= 0 and village.grid[self.position_n, left] == " ":
            self.clear_character(village)
            self.position_m = left
            self.place_character(village)

        self.last_moved_direction = "A"

    def move_down(self, village):

        if self.check_death():
            return

        down = self.position_n + 1

        if down < village.n and village.grid[down, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = down
            self.place_character(village)

        self.last_moved_direction = "S"

    def move_right(self, village):

        if self.check_death():
            return

        right = self.position_m + 1

        if right < village.m and village.grid[self.position_n, right] == " ":
            self.clear_character(village)
            self.position_m = right
            self.place_character(village)

        self.last_moved_direction = "D"

    def attack(self, village):

        if self.check_death():
            return

        m = self.position_m
        n = self.position_n

        size_m = village.m
        size_n = village.n

        if m + 1 < size_m:
            building1 = village.get_building(n, m + 1)
        if m - 1 >= 0:
            building2 = village.get_building(n, m - 1)
        if n + 1 < size_n:
            building3 = village.get_building(n + 1, m)
        if n - 1 >= 0:
            building4 = village.get_building(n - 1, m)

        for building in [building1, building2, building3, building4]:
            if building is None:
                continue
            # Damage this building
            building.hitpoints -= self.damage

            # can only hit one building at one point
            return

    def check_death(self):
        if self.health <= 0:
            return True
        else:
            return False

    def get_position(self):
        return (self.position_n, self.position_m)

    def render_health(self):

        print(Fore.LIGHTRED_EX, end="")
        for i in range(self.health):
            print("=", end="")
        if self.health >= 0:
            print(f"> {self.health} {Style.RESET_ALL}")
        else:
            print(f"> 0 {Style.RESET_ALL}")


class King(Character):
    def __init__(self, village):
        """
        King's damage assumed to be 15
        King's position by default assumed to be (15, 1)
        """
        super().__init__(15, "K")
        self.init_position(15, 1)
        self.place_character(village)

    def leviathan_axe(self, village):
        """
        Deal damage to all buildings within 5 tile radius
        """

        i = self.position_n
        j = self.position_m

        for building in village.buildings:
            for tup in building.position:
                if (i - tup[0]) ** 2 + (j - tup[1]) ** 2 <= 25:
                    building.hitpoints -= self.damage
                    break


class Queen(Character):
    def __init__(self, village):
        """
        Queen's damage assumed to be 10 (less than King's)
        Queen's position by default assumed to be (15, 1)
        """
        super().__init__(10, "Q")
        self.init_position(15, 1)
        self.place_character(village)

    def attack(self, village):
        """
        Override King's attack
        """

        if self.check_death():
            return

        direction = self.last_moved_direction

        if direction == "W":
            x = self.position_n - 8
            y = self.position_m
        elif direction == "A":
            x = self.position_n
            y = self.position_m - 8
        elif direction == "S":
            x = self.position_n + 8
            y = self.position_m
        else:
            x = self.position_n
            y = self.position_m + 8

        buildings_in_range = []

        # Area of effect
        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                building = village.get_building(i, j)
                if building is not None:
                    buildings_in_range.append(building)

        buildings_in_range = set(buildings_in_range)

        for building in buildings_in_range:
            # Damage this building
            building.hitpoints -= self.damage


class Barbarian(Character):
    def __init__(self, damage=5, display_character="#"):
        super().__init__(damage, display_character)
        self.counter = 1  # Number of attacks per timestamp
        self.movement_speed = 1

    def reset_counter(self):
        self.counter = 1

    """
    Override parent class behaviour (Polymorphism)

    move methods
    """

    def attack(self, village, i, j):
        """
        Attack at position i, j
        """
        if self.counter == 0:
            # No more attacks possible in this timestamp
            return

        # else decrement counter
        self.counter -= 1

        building = village.get_building(i, j)

        # Damage this building
        building.hitpoints -= self.damage

        return

    def move_up(self, village):

        up = self.position_n - 1

        if up >= 0:

            if (
                village.grid[up, self.position_m] == " "
                or village.grid[up, self.position_m] == "#"
                or village.grid[up, self.position_m] == "A"
            ):
                self.clear_character(village)
                self.position_n = up
                self.place_character(village)
            elif village.grid[up, self.position_m] == "W":
                self.attack(village, up, self.position_m)

    def move_left(self, village):

        left = self.position_m - 1

        if left >= 0:
            if (
                village.grid[self.position_n, left] == " "
                or village.grid[self.position_n, left] == "#"
                or village.grid[self.position_n, left] == "A"
            ):
                self.clear_character(village)
                self.position_m = left
                self.place_character(village)
            elif village.grid[self.position_n, left] == "W":
                self.attack(village, self.position_n, left)

    def move_down(self, village):

        down = self.position_n + 1

        if down < village.n:
            if (
                village.grid[down, self.position_m] == " "
                or village.grid[down, self.position_m] == "#"
                or village.grid[down, self.position_m] == "A"
            ):
                self.clear_character(village)
                self.position_n = down
                self.place_character(village)
            elif village.grid[down, self.position_m] == "W":
                self.attack(village, down, self.position_m)

    def move_right(self, village):

        right = self.position_m + 1

        if right < village.m:
            if (
                village.grid[self.position_n, right] == " "
                or village.grid[self.position_n, right] == "#"
                or village.grid[self.position_n, right] == "A"
            ):
                self.clear_character(village)
                self.position_m = right
                self.place_character(village)
            elif village.grid[self.position_n, right] == "W":
                self.attack(village, self.position_n, right)

    def get_nearest_building(self, village):
        """Return current and nearest building coordinates"""

        min_distance = None
        min_distance_coordinate = None

        i = self.position_n
        j = self.position_m

        for building in village.buildings:
            if building.display_character == "W":
                continue

            for position in building.position:

                distance = (i - position[0]) ** 2 + (j - position[1]) ** 2

                if min_distance is None or min_distance > distance:
                    min_distance = distance
                    min_distance_coordinate = position

        return i, j, min_distance_coordinate

    def move_towards_nearest_building(self, village, i, j, min_distance_coordinate):
        """Move towards the min_distance_coordinate"""

        if i < min_distance_coordinate[0] - 1:
            self.move_down(village)
        elif i > min_distance_coordinate[0] + 1:
            self.move_up(village)
        else:
            if j < min_distance_coordinate[1] - 1:
                self.move_right(village)

            elif j > min_distance_coordinate[1] + 1:
                self.move_left(village)
            else:
                if (
                    i == min_distance_coordinate[0] - 1
                    and j == min_distance_coordinate[1] + 1
                ):
                    self.move_left(village)
                elif (
                    i == min_distance_coordinate[0] - 1
                    and j == min_distance_coordinate[1] - 1
                ):
                    self.move_right(village)
                elif (
                    i == min_distance_coordinate[0] + 1
                    and j == min_distance_coordinate[1] - 1
                ):
                    self.move_right(village)
                elif (
                    i == min_distance_coordinate[0] + 1
                    and j == min_distance_coordinate[1] + 1
                ):
                    self.move_left(village)
                else:
                    self.attack(
                        village, min_distance_coordinate[0], min_distance_coordinate[1]
                    )

    def move_once(self, village):
        if self.check_death():
            return

        i, j, min_distance_coordinate = self.get_nearest_building(village)

        if min_distance_coordinate is None:
            return

        self.move_towards_nearest_building(village, i, j, min_distance_coordinate)

    def move(self, village):
        for _ in range(self.movement_speed):
            self.move_once(village)


class Archer(Barbarian):
    def __init__(self):
        super().__init__(damage=2.5, display_character="A")
        self.health = 50
        self.movement_speed = 2
        self.range = 8

    """
    Override move_once of barbarian
    """

    def move_once(self, village):
        if self.check_death():
            return

        i, j, min_distance_coordinate = self.get_nearest_building(village)

        if min_distance_coordinate is None:
            return

        distance = (i - min_distance_coordinate[0]) ** 2 + (
            j - min_distance_coordinate[1]
        ) ** 2

        if distance <= self.range**2:
            # Attack
            self.attack(village, min_distance_coordinate[0], min_distance_coordinate[1])
        else:
            self.move_towards_nearest_building(village, i, j, min_distance_coordinate)
