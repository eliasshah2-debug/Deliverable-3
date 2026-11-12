#Task 2: The Dice Class

#To make damage random, we created "Dice" class that can represent any dice with n sides (n ≥ 2, default 6). "roll()" returns a random number between 1 and the number of sides, using "random,randint". "repr" returns a readable string like "Dice(sides=6)". "Call" lets us roll the dice by calling the object diretly , so "d20()" gives the same result as "d20.roll()".

#If the number of sides is not an integer of at least 2, a "ValueError" is raised.


import random

class Dice:
    """An n-sided dice (n>= 2). Default is a normal 6-sided dice."""

    def __init__(self, sides: int = 6):
        if not isinstance(sides, int) or sides < 2:
            raise ValueError("A dice must have an integer number of sides >= 2")
        self._sides = sides

    @property
    def sides(self) -> int:
        """Number of sides (read-only)"""
        return self._sides

    def roll(self) -> int:
        """Roll the dice and return a number between 1 and sides."""
        return random.randint(1, self.sides)

    def __call__(self) -> int: 
        """Calling the object rolls it: d20() does the same as d20.roll()."""
        return self.roll()

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"