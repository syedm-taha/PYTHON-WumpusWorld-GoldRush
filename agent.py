

class KB_Agent:
    def __init__(self, env):
        self.env = env
        self.position = (0, 0)
        self.kb = {}  # Knowledge base to store known facts
        self.visited = set()
        self.arrows = 1
        self.gold_collected = False
        self.path = []

    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            new_pos = (x-1, y)
        elif direction == 'down':
            new_pos = (x+1, y)
        elif direction == 'left':
            new_pos = (x, y-1)
        elif direction == 'right':
            new_pos = (x, y+1)

        if self.env.is_valid_position(*new_pos):
            self.position = new_pos
            self.update_kb(new_pos)
            self.path.append(new_pos)
            self.visited.add(new_pos)

    def update_kb(self, pos):
        percepts = self.env.get_percepts(*pos)
        self.kb[pos] = percepts
        if 'Glitter' in percepts:
            self.pick_up_gold()

    def shoot_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            # Assuming Wumpus is killed if the arrow is shot
            # In a real scenario, we should check if Wumpus is in the line of fire
            print("Arrow shot!")
            return True
        return False

    def pick_up_gold(self):
        if 'Glitter' in self.kb.get(self.position, []):
            self.gold_collected = True
            # print("Gold collected!")
            return True
        return False

    def make_decision(self):
        # Explore unvisited neighbors first
        x, y = self.position
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in self.visited and self.env.is_valid_position(nx, ny):
                self.move_to(nx, ny)
                return

        # If all neighbors are visited, move to a random visited position
        if self.path:
            self.position = self.path.pop()

    def move_to(self, x, y):
        if x < self.position[0]:
            self.move('up')
        elif x > self.position[0]:
            self.move('down')
        elif y < self.position[1]:
            self.move('left')
        elif y > self.position[1]:
            self.move('right')

    def play_game(self):
        while not self.gold_collected:
            self.make_decision()
            self.print_kb()
            if 'Stench' in self.kb[self.position]:
                self.shoot_arrow()
        print("Game over! Gold collected.")

    def print_kb(self):
        for pos, percepts in self.kb.items():
            print(f"Position {pos}: Percepts: {percepts}")
