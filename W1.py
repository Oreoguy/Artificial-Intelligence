import numpy as np

# Define the symbols for different types of rooms
WUMPUS = 'W'
PIT = 'P'
BREEZE = 'B'
STENCH = 'S'
GOLD = 'G'
SAFE = ' '
UNKNOWN = '?'

# Define the possible directions the agent can move
NORTH = 'N'
EAST = 'E'
WEST = 'W'
SOUTH = 'S'

# Define the action symbols
MOVE = 'M'
SHOOT = 'S'
GRAB = 'G'
CLIMB = 'C'

class WumpusWorld:
    def __init__(self, n):
        self.n = n
        self.env_matrix = np.full((n, n), UNKNOWN)  # the environment matrix
        self.kb_matrix = np.full((n, n), UNKNOWN)  # the knowledge base matrix
        self.current_room = (1, 1)  # the agent starts in the top-left room
        self.visited_rooms = set()  # the set of rooms the agent has visited
        self.actions = []  # the sequence of actions taken by the agent

        # Place the Wumpus randomly in the environment
        wumpus_room = self.random_room()
        self.env_matrix[wumpus_room] = WUMPUS

        # Place the pits randomly in the environment
        num_pits = np.random.randint(n) + 1
        for i in range(num_pits):
            pit_room = self.random_room()
            while self.env_matrix[pit_room] != UNKNOWN:
                pit_room = self.random_room()
            self.env_matrix[pit_room] = PIT
            # Add breeze to adjacent rooms
            for adj_room in self.adjacent_rooms(pit_room):
                if self.env_matrix[adj_room] == UNKNOWN:
                    self.env_matrix[adj_room] = BREEZE

        # Place the gold randomly in the environment
        gold_room = self.random_room()
        while self.env_matrix[gold_room] != UNKNOWN:
            gold_room = self.random_room()
        self.env_matrix[gold_room] = GOLD

        # Add stench to adjacent rooms of the Wumpus
        for adj_room in self.adjacent_rooms(wumpus_room):
            if self.env_matrix[adj_room] == UNKNOWN:
                self.env_matrix[adj_room] = STENCH

    def random_room(self):
        """Return a randomly chosen room."""
        row = np.random.randint(self.n)
        col = np.random.randint(self.n)
        return (row, col)

    def adjacent_rooms(self, room):
        """Return a list of adjacent rooms to the given room."""
        row, col = room
        adj_rooms = []
        if row > 0:
            adj_rooms.append((row - 1, col))  # north
        if row < self.n - 1:
            adj_rooms.append((row + 1, col))  # south
        if col > 0:
            adj_rooms.append((row, col - 1))  # west
        if col < self.n - 1:
            adj_rooms.append((row, col + 1))  # east
        return adj_rooms
    
    def update_kb_matrix(self):
        """Update the knowledge base matrix based on the current room."""
        row, col = self.current_room

            # Update the current room in the knowledge base matrix
        self.kb_matrix[row, col] = self.env_matrix[row, col]

        # Update adjacent rooms based on current room's contents
        if self.env_matrix[row, col] == BREEZE:
            for adj_room in self.adjacent_rooms(self.current_room):
                if self.kb_matrix[adj_room] == UNKNOWN:
                    self.kb_matrix[adj_room] = PIT
        elif self.env_matrix[row, col] == STENCH:
            for adj_room in self.adjacent_rooms(self.current_room):
                if self.kb_matrix[adj_room] == UNKNOWN:
                    self.kb_matrix[adj_room] = WUMPUS
        elif self.env_matrix[row, col] == GOLD:
            self.actions.append(GRAB)

    # Mark current room as visited
        self.visited_rooms.add(self.current_room)


