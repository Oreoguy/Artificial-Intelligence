import numpy as np

# Define the environment matrix with the actual facts about each room
# 0 = nothing, 1 = breeze, 2 = stench, 3 = breeze and stench, 4 = pit, 5 = Wumpus, 6 = gold
environment_matrix = np.array([
    [2, 1, 0, 0],
    [4, 2, 1, 0],
    [0, 4, 2, 1],
    [2, 0, 1, 5],
    [0, 4, 0, 0],
    [0, 0, 0, 6]
])

# Define the agent's knowledge matrix, initially empty
knowledge_matrix = np.zeros_like(environment_matrix)

# Define the utility function that assigns values to rooms based on their likelihood of containing gold
def utility(room):
    if room == 6:
        return 100
    elif room == 4 or room == 5:
        return -100
    elif room == 3 or room == 2:
        return -1
    elif room == 1:
        return -0.5
    else:
        return 0

# Define the function to perform reasoning and make a decision about the next room to visit
def choose_next_room(current_room):
    # Get the indices of the adjacent rooms
    adjacent_indices = [(current_room[0]-1, current_room[1]), (current_room[0]+1, current_room[1]), 
                        (current_room[0], current_room[1]-1), (current_room[0], current_room[1]+1)]
    
    # Eliminate rooms that are known to be unsafe based on current knowledge
    safe_indices = []
    for idx in adjacent_indices:
        if idx[0] < 0 or idx[0] >= environment_matrix.shape[0] or idx[1] < 0 or idx[1] >= environment_matrix.shape[1]:
            continue  # skip if index is out of bounds
        if knowledge_matrix[idx] == 4 or knowledge_matrix[idx] == 5:
            continue  # skip if room is known to contain a pit or Wumpus
        safe_indices.append(idx)
    
    # If all adjacent rooms are unsafe, backtrack to the previous room
    if len(safe_indices) == 0:
        return None
    
    # Compute the expected utility of each safe room based on current knowledge
    utilities = []
    for idx in safe_indices:
        room = environment_matrix[idx]
        utility_val = utility(room)
        for adj_idx in [(idx[0]-1, idx[1]), (idx[0]+1, idx[1]), (idx[0], idx[1]-1), (idx[0], idx[1]+1)]:
            if adj_idx[0] < 0 or adj_idx[0] >= environment_matrix.shape[0] or adj_idx[1] < 0 or adj_idx[1] >= environment_matrix.shape[1]:
                continue  # skip if index is out of bounds
            if knowledge_matrix[adj_idx] == 4 or knowledge_matrix[adj_idx] == 5:
                utility_val -= 50  # subtract a penalty if an adjacent room is known to contain a pit or Wumpus
        utilities.append((idx, utility_val))
    
    # Choose the safe room with the highest expected utility
    next_room = max(utilities, key=lambda x: x[1])[0]
    
    return next_room

# Example usage
