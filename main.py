---

### `main.py`
```python
"""
Main Game Loop - Buggy Quest
WARNING: Contains intentional bugs for the collaborative repair challenge!
"""

import sys
from player import Player
# BUG 1: Import error - scoreboard function name doesn't match scoreboard.py
from scoreboard import display_scores, save_score 

def game_loop():
    print("=" * 40)
    print(" 🏰 WELCOME TO BUGGY QUEST 🏰 ")
    print("=" * 40)
    
    player_name = input("Enter your hero's name: ")
    hero = Player(player_name)

    # BUG 2: Logical error in turn counter loop (causes infinite loop or early exit)
    turn = 0
    while turn < 3:
        print(f"\n--- Turn {turn} ---")
        print("1. Fight Monster")
        print("2. Rest & Heal")
        print("3. Quit")
        
        choice = input("What will you do? (1-3): ")
        
        if choice == "1":
            damage_dealt = hero.attack()
            damage_taken = 15
            hero.take_damage(damage_taken)
            print(f"You dealt {damage_dealt} damage and took {damage_taken} damage!")
        elif choice == "2":
            # BUG 3: Calls a method on Player that doesn't exist or has wrong signature
            hero.heal() 
        elif choice == "3":
            print("You fled the dungeon!")
            break
        else:
            print("Invalid choice!")

        # MISSING: turn increment is missing, causing infinite loop!
        # turn += 1 

    print("\nGame Over!")
    # BUG 4: Missing arguments or broken function call
    save_score(hero.name, hero.gold) 
    display_scores()

if __name__ == "__main__":
    game_loop()
