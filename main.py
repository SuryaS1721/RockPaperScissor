import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    # Strategy 1: Counter the most common move
    most_common = max(set(opponent_history), key=opponent_history.count)
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[most_common]

# Debugging: Test the function with print statements
if __name__ == "__main__":
    print(player(""))  # First move (random)
    #print(player("R")) # Should return "P" (counters "R")
    #print(player("P")) # Should return "S" (counters "P")
    #print(player("S")) # Should return "R" (counters "S")
