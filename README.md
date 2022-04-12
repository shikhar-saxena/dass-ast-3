# DASS Assignment 3.2: Terminal Python game using OOPS concepts

## Quick Start and Game Rules

| Key         | Description |
| ----------- | ----------- |
| 0           | To choose King as your character       |
| 1   | (beginning of game) To choose Archer Queen as your character. Later, to spawn barbarian from spawning point `1`        |
| 2   | To spawn barbarian from spawning point `2`        |
| 3   | To spawn barbarian from spawning point `3`        |
| 4   | To spawn archer from spawning point `1`        |
| 5   | To spawn archer from spawning point `2`        |
| 6   | To spawn archer from spawning point `3`        |
| 7   | To spawn balloon from spawning point `1`        |
| 8   | To spawn balloon from spawning point `2`        |
| 9   | To spawn balloon from spawning point `3`        |
| `space`   | For character attack; King attacks buildings in adjacent cells and Archer queen attacks in AoE of 5x5 as described in assignment doc.        |
| W | To move up (for character)        |
| A | To move left (for character)        |
| S | To move down (for character)        |
| D | To move right (for character)        |
| `^C` | To abort game        |
| L | To execute Leviathan axe (if character chosen is king)        |
| R | Rage Spell (only one rage spell available in each level)        |
| H | Heal Spell (only one heal spell available in each level)        |


Run the game using `python3 game.py` in your terminal. Full Screen would be preferred for the game to render properly. To exit the game use `Ctrl + C`.

Choose your character: 0 for king (displayed as `K`) and 1 for Queen (displayed as `Q`). For moving use W, A, S, D keys for up, left, down and right movement respectively.

King can only attack a building if that building is adjacent to its position on the village. For attacking a building press spacebar. If King is adjacent to many buildings then the order of its attack is right building, left building, building below (on the next row), building above (on the previous row).

Queen on the other hand attacks in an area of effect as described in the problem doc. For attacking use spacebar.

Also, you can use special attack using key `L` (For King). This special attack is called King’s leviathan axe (explained in the Bonus section of this file). 

The color of the building shows it's health. It will go from green to yellow to red as its health will decrease. If the building is completely destroyed, then it will no longer show on the village.

Character's healthbar will be shown on the top.

There are Cannons in the village, of size 1x1, (displayed as `C`) that can attack upto a range of 6 tiles.

All distances in the game are measured as **euclidean distances** (if needed to check whether a troop is in range and so on).

On the village boundaries', there are three points `1`, `2` and `3` which are the spawning points for your army. Army includes Barbarians, Archers and Balloons. The Barbarians, Archers and Balloons are displayed as `#`, `A` and `B` respectively on the village.

The movement of all Troops is automated. They will attack the buildings in the village. There health is shown by their color as well. As their health decreases, their color changes from dark to light or more specifically it changes from Blue to lightblue to lightcyan to white (if they are dead). Dead army (king, queen or troops) are shown on the map (if the game is not over yet). But they can neither move nor attack further.

Multiple Troops can be on the same cell in the village. However, they are not allowed to move diagonally. If their speed is double etc, it might seem like they are moving diagonally. Also, the color shown for a cell with many troops, will be the color of the first troop (as stored in our list of troops).

If your troops destroy all the buildings (except the walls) then you won the level.

Otherwise if the cannons and wizard towers are able to kill all the troops (including your Character) then you lose (Defeat).

## Code

- `character.py` contains `Character`, `King`, `Queen`, `Barbarian`, `Archer`, `Balloon` class.
- `grid.py` contains `Village`, `Spawning_Point`, `Building` and associated subclasses.
- `input.py`: sample input file (provided by TAs)
- `game.py`: contains the `Game` class and running this file will start the game

## Requirements completed

All requirements *except* **Replay** have been completed. 

## Assignment 3.2 requirements

### Modifications in Assignment 3.1 code

Cannon's size is changed from 2x2 to 1x1. Also, cannon's damage was changed to 7.

### Limit on troops

In each level, the player can only spawn at max six barbarians, three archers and three balloons.

### Archer

Archers move like barbarians except if the nearest building is in their range, then they will stop moving and attack from there itself. Archer range assumed to be 8.

### Balloon

Balloons can fly over buildings and reach the building they want to attack. Balloon will try to attack the nearest cannon or wizard tower first. If all cannons and wizard towers have been destroyed, then balloon will move towards destroying other non-wall buildings. Balloons need to be adjacent to the target Building, in order to attack it. Cannon cannot attack them. Only Wizard towers can attack them.

### Wizard Tower

Wizard tower is assumed to be able to attack all troops. Attacks using AoE in a 3x3 tile area with the target troop on the centre of this area. If multiple troops present in the AoE, then all are affected.

- Size 1x1
- Denoted as `Z` on the village
- Range and Damage same as cannon

## OOPS Concepts

### Inheritance

We have implemented one Building class (in `grid.py`) which has been inherited by other sub-classes like Hut, Cannon, Town Hall, etc. 

### Polymorphism

We have made a Character class (in `character.py`) which contains move functionalities (for the King and Queen). These functionalities have been overridden for the Barbarian.

### Encapsulation

We have strictly followed the class-object approach for all the requirements in this assignment.

### Abstraction

Intuitive functionalities like `move_up`, `attack`, etc. are present for King and Barbarians.

## Village

**Assumptions** made:

- n and m assumed to be 38 and 40 respectively. Here n is the number of rows and m is the number of columns.
- Spawning points are on the border of the village (and not inside the village)
- Huts are of size 1x1 (displayed as `H`) and a total of nine huts are present in the village
- Cannons are of size 1x1 (displayed as `C`).
- Range of the cannon is upto 6 tiles
- Damage per attack for the cannon is about 7 
- Town Hall displayed as `T`
- Walls displayed as `W`
- The health for all buildings (and also for king/queen and Barbarians/balloons) are all equal to 100 (by default). For archers, the health is 50 (half of barbarians). We haven't given a variable fixed total-health (for different buildings and character). Since our fixed total-health is 100, the `health` characteristic itself gives the percentage health at each moment (except for archer which has been dealt with differently in the codebase).

## King

**Assumptions** made:

- King's damage is assumed to be 15
- King's position by default is assumed to be (15, 1) (zero-based indexing).
- King denoted by `K`

## Archer Queen

**Assumptions** made:

- Queen's damage is assumed to be 10
- Queen's position by default is assumed to be (15, 1) (zero-based indexing).
- By default, last moved direction of archer queen is taken to be right (when queen hasn't moved at all).
- Queen denoted by `Q`

## Troops

Explained above.

## Game Endings

Game endings are displayed once the game is over (whether victory or defeat).

Game goes on for three levels. If defeated in some level, then the game ends with Defeat. Victory only happens if we win all the three levels. 

### Levels

**Level 1**: 3 cannons and 3 wizard towers

**Level 2**: 4 cannons and 4 wizard towers

**Level 3**: 5 cannons and 5 wizard towers

## Spells

### Heal spell

Increases health to 150% of the current health (capped at max health) for alive troops (including king/archer-queen if they are alive).

### Rage spell

For each alive troop (including King/Archer-Queen), if the damage does not exceed 100 (max hitpoints of any building) on doubling (so that they cannot oneshot any building); then the damage is set to this value (double of initial damage value) and movement speed is also doubled for this troop.


## Bonus

### King's leviathan axe

On pressing `L` key on the keyboard the king can attack on all buildings in the range of 5 tiles. The damage per time stamp is the same as the damage the king can do normally.
