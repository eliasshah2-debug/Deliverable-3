#"Object-oriented game simulator Based on game_simulator_v1.py by Turid, NMBU, 2026 Task 1: Updating Character class

#In the original version, "attack()" changed the target's prtoected attribute "_hp" directly. This breaks encapsulation, because one object should not modify another object's private data.

#To fix this, we added: "Take_damage(amount)" = reduces the character's own HP, burt never below 0. "heal(amount)" = increases the character's own HP, but never above "hp_max". "is_alive" = a read-only property that returns "true" if HP is above 0.

#"attack()" now calls "target.take_damage()", so each character is responsible for its own HP.


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Inititialise the Character

        Args:
            name (str): The name of the character
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, amount: int) -> None:
        """
        Reduce the character's own HP by amount.
        HP cannot end up lower than 0.
        """
        self._hp -= amount 
        self._hp = max(self._hp, 0)

    def heal(self, amount: int) -> None:
        """
        Increase the character's own HP by amount.
        HP cannot end up higher than hp_max.
        """
        self._hp += amount 
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target) -> None:
        """Attack target character, which then takes damage"""
        target.take_damage(self.damage)

    def introduce(self) -> None: 
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"Character name={self.name} hp={self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP"""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property: True if the character has more than 0 HP"""
        return self._hp > 0 
    