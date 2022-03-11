# from grid import Village


class Character:
    def __init__(self, damage, speed, display_character):
        self.damage = damage
        self.health = 100
        self.speed = speed
        self.display_character = display_character
        # self.inputs = inputs

    def init_position(self, position_n, position_m):
        self.position_n = position_n
        self.position_m = position_m

    def place_character(self, village):
        village.grid[self.position_n, self.position_m] = self.display_character

    def clear_character(self, village):
        village.grid[self.position_n, self.position_m] = " "

    def move(self, village):
        pass

    def move_up(self, village):
        up = self.position_n - 1

        if up >= 0 and village.grid[up, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = up
            self.place_character(village)

    def move_left(self, village):
        left = self.position_m - 1

        if left >= 0 and village.grid[self.position_n, left] == " ":
            self.clear_character(village)
            self.position_m = left
            self.place_character(village)

    def move_down(self, village):
        down = self.position_n + 1

        if down < village.n and village.grid[down, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = down
            self.place_character(village)

    def move_right(self, village):

        right = self.position_m + 1

        if right < village.m and village.grid[self.position_n, right] == " ":
            self.clear_character(village)
            self.position_m = right
            self.place_character(village)

    def attack(self, village):
        priority = ["T", "C", "H", "W"]

        # TODO: priority in attack

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


class King(Character):
    def __init__(self, village):
        """
        King's damage assumed to be 20
        King's position by default assumed to be (15, 15)
        """
        super().__init__(20, 10, "K")
        self.init_position(15, 1)
        self.place_character(village)

    # TODO: character Speed
    # TODO: Input handling

    # Override
    def move(self, village, input_ch):

        if input_ch == "w" or input_ch == "W":
            self.move_up(village)
        elif input_ch == "a" or input_ch == "A":
            self.move_left(village)
        elif input_ch == "s" or input_ch == "S":
            self.move_down(village)
        elif input_ch == "d" or input_ch == "D":
            self.move_down(village)
