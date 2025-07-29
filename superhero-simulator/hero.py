#Superhero Battle Simulator - Manica Thea
import random
from ability import Ability
from armor import Armor 

# hero.py
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
        print(f"{self.name} battles {opponent.name}!")
        winner = random.choice([self, opponent])
        print(f"{winner.name} wins the battle!")
        
    def add_ability(self, ability):
        self.abilities.append(ability)

    def sum_of_attacks(self):
        total_damage = 0 
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero1 = Hero("Spiderman", 200)
    
    my_hero.battle(my_hero1)    

    
