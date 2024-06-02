import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_game():
    first_roll = roll_dice()
    
    if first_roll in [7, 11]:
        return "Player wins on first roll!"
    elif first_roll in [2, 3, 12]:
        return "Casino wins on first roll!"
    
    goal_number = first_roll
    print(f"Goal number is: {goal_number}")
    
    while True:
        roll = roll_dice()
        print(f"Rolled: {roll}")
        
        if roll == goal_number:
            return "Player wins!"
        elif roll == 7:
            return "Player loses!"

result = play_game()
print(result)
