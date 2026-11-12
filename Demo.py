from dice import Dice
from items import Weapon
from character import Character, Warrior, Mage
from battle import Battle
 
hero = Character("Hero", hp_max=50, damage=12)
goblin = Character("Goblin", hp_max=30, damage=5)
hero.attack(goblin); goblin.attack(hero)
print(hero); print(goblin)
hero.heal(100); print("After heal:", hero)
hero.attack(goblin); hero.attack(goblin)
print(goblin, "| alive?", goblin.is_alive)
try:
    goblin.is_alive = True
except AttributeError as e:
    print("AttributeError:", e)
print(Dice(), Dice(sides=20))
 
sword, staff = Weapon("Sword", Dice(8)), Weapon("Staff", Dice(4))
print(sword)
w, m = Warrior("Conan", weapon=sword), Mage("Merlin", weapon=staff)
print(w); print(m)
Battle(w, m).simulate_battle()
print(); Battle(Character("Plain Joe"), Mage("Gandalf")).simulate_battle()
 
m2 = Mage("Test"); t = Character("Dummy", hp_max=1000)
for _ in range(5): m2.attack(t)
print("mana trace ok:", m2.mana, "| Warrior armor 5 vs dmg 3 ->", end=" ")
w2 = Warrior("W"); w2.take_damage(3); print(w2.hp)