import random as rand

class Environment:
    def __init__(self, size=4):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.place_pits()
        self.place_wumpus()
        self.place_gold()
        self.agent_position = (0, 0)

    def place_pits(self):
        num_pits = rand.randint(1, self.size)
        for _ in range(num_pits):
            x, y = rand.randint(0, self.size-1), rand.randint(0, self.size-1)
            self.grid[x][y] = 'Pit'

    def place_wumpus(self):
        x, y = rand.randint(0, self.size-1), rand.randint(0, self.size-1)
        self.grid[x][y] = 'Wumpus'

    def place_gold(self):
        x, y = rand.randint(0, self.size-1), rand.randint(0, self.size-1)
        self.grid[x][y] = 'Gold'

    def get_percepts(self, x, y):
        percepts = []
        if self.grid[x][y] == 'Pit':
            percepts.append('Breeze')
        if self.grid[x][y] == 'Wumpus':
            percepts.append('Stench')
        if self.grid[x][y] == 'Gold':
            percepts.append('Glitter')

        # Check adjacent cells for breeze and stench
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] == 'P':
                    percepts.append('Breeze')
                if self.grid[nx][ny] == 'Wumpus':
                    percepts.append('Stench')

        return percepts

    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
