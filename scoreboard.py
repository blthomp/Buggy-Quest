"""
Scoreboard Module
"""

HIGH_SCORES_FILE = "scores.txt"

# BUG 8: Function name mismatch with main.py import
def record_player_score(name, score):
    """Saves player score to file."""
    # BUG 9: File opened in read mode instead of append mode ('r' vs 'a')
    with open(HIGH_SCORES_FILE, "r") as f:
        f.write(f"{name}:{score}\n")

def display_scores():
    """Reads and prints all saved scores."""
    try:
        with open(HIGH_SCORES_FILE, "r") as f:
            lines = f.readlines()
            print("\n--- HIGH SCORES ---")
            for line in lines:
                name, score = line.strip().split(":")
                print(f"Hero: {name} | Score: {score}")
    except FileNotFoundError:
        print("\nNo high scores recorded yet!")
