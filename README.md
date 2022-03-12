# DASS Assignment 3.1: Terminal Python game using OOPS concepts

## Quick Start and Game Rules

Run the game using `python3 game.py` in your terminal. Full Screen would be preferred for the game to render properly. To exit the game use `Ctrl + C`.

Your character is the king (displayed as `K`). For moving the king use W, A, S, D keys for up, left, down and right movement respectively.

King can only attack a building if that building is adjacent to its position on the village. For attacking a building press spacebar. If King is adjacent to many buildings then the order of its attack is right building, left building, building below (on the next row), building above (on the previous row).

Also, you can use special attack using key `L`. This special attack is called King’s leviathan axe (explained in the Bonus section of this file). 

The color of the building shows it's health. It will go from green to yellow to red as its health will decrease. If the building is completely destroyed, then it will no longer show on the village.

King's healthbar will be shown on the top.

There are Cannons in the village, of size 2x2, (displayed as `C` in each cell in the 2x2 subgrid) that can attack upto a range of 6 tiles (here the range is measured from the top left cell of the cannon).

All distances in the game are measured as **euclidean distances** (if needed to check whether a troop is in range and so on).

On the village boundaries', there are three points `1`, `2` and `3` which are the spawning points for your army aka barbarians. Press `1`, `2` or `3` respectively to spawn barbarians at the respective spawning point. The Barbarians are displayed as `#` on the village.

The movement of the Barbarians is automated. They will attack the buildings in the village. There health is shown by their color as well. As their health decreases, their color changes from dark to light or more specifically it changes from Blue to lightblue to lightcyan to white (if they are dead).

Multiple Barbarians can be on the same cell in the village. However, they are not allowed to move diagonally. Also, the color shown for a cell with many barbarians, will be the color of the first barbarian (as stored in our list of troops).

Dead troops (king or barbarians) are shown on the map (if the game is not over yet). But they can neither move nor attack further.

If your troops destroy all the buildings (except the walls) then you won the game (Victory).

Otherwise if the cannons are able to kill all the troops (including your King) then you lose (Defeat).

## Code

- `character.py` contains `Character`, `King` and `Barbarian` class.
- `grid.py` contains `Village`, `Spawning_Point`, `Building` and associated subclasses.
- `input.py`: sample input file (provided by TAs)
- `game.py`: contains the `Game` class and running this file will start the game

## Requirements completed

All requirements *except* **Spells** and **Replay** have been completed. 

## OOPS Concepts

### Inheritance

We have implemented one Building class (in `grid.py`) which has been inherited by other sub-classes like Hut, Cannon, Town Hall, etc. 

### Polymorphism

We have made a Character class (in `character.py`) which contains move functionalities (for the King). These functionalities have been overridden for the Barbarian.

### Encapsulation

We have strictly followed the class-object approach for all the requirements in this assignment.

### Abstraction

Intuitive functionalities like `move_up`, `attack`, etc. are present for King and Barbarians.

## Village

**Assumptions** made:

- n and m assumed to be 38 and 40 respectively. Here n is the number of rows and m is the number of columns.
- Spawning points are on the border of the village (and not inside the village)
- Huts are of size 1x1 (displayed as `H`) and a total of nine huts are present in the village
- Cannons are of size 2x2 (displayed as `C`) and a total of three cannons are present in the village
- Range of the cannon is upto 6 tiles (measured from the top left cell belonging to the cannon)
- Damage per attack for the cannon is about 10 
- Town Hall displayed as `T`
- Walls displayed as `W`
- The health for all buildings (and also for king and Barbarians) are all equal to 100 (by default). We haven't given a variable fixed total-health (for different buildings and character). Since our fixed total-health is 100, the `health` characteristic itself gives the percentage health at each moment.

## King

**Assumptions** made:

- King's damage is assumed to be 15
- King's position by default is assumed to be (15, 1) (zero-based indexing).
- King denoted by `K`

## Barbarians

Explained above.

## Game Endings

Game endings are displayed once the game is over (whether victory or defeat).

## Bonus

### King's leviathan axe

On pressing `L` key on the keyboard the king can attack on all buildings in the range of 5 tiles. The damage per time stamp is the same as the damage the king can do normally.

