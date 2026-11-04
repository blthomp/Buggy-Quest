"""
Player Module
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.max_health = 100
        self.gold = 10
        # BUG 5: Syntax error or undefined attribute elsewhere

    def attack(self):
        # Returns damage dealt
        return 20

    def take_damage(self, amount):
        self.health -= amount
        # BUG 6: Health can go below 0 without handling player death
        print(f"Current Health: {self.health}/{self.max_health}")

    # BUG 7: Missing heal parameter or incorrect logic
    def heal(self):
        # Restores health, but doesn't cap at max_health and adds negative numbers correctly
        self.health += 25
        print(f"Healed! Current Health: {self.health}")
