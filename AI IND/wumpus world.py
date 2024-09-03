import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_position = (0, 0)
        self.wumpus_position = self.generate_random_position()
        self.gold_position = self.generate_random_position() 
        self.pit_positions = [self.generate_random_position() for _ in range(3)]

    def generate_random_position(self):
        return random.randint(0, self.size-1), random.randint(0, self.size-1)

    def check_agent_status(self):
        if self.agent_position == self.wumpus_position:
            return "You were eaten by the Wumpus! Game over."
        elif self.agent_position == self.gold_position:
            return "You found the gold! You win!"
        elif self.agent_position in self.pit_positions:
            return "You fell into a pit! Game over."
        else:
            return "You are safe."

    def move(self, direction):
        x, y = self.agent_position
        if direction == 'up' and x > 0:
            self.agent_position = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_position = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_position = (x, y + 1)
        else:
            print("Invalid move! Please try again.")

    def print_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_position:
                    print('A', end=' ')
                elif (i, j) == self.wumpus_position:
                    print('W', end=' ')
                elif (i, j) == self.gold_position:
                    print('G', end=' ')
                elif (i, j) in self.pit_positions:
                    print('P', end=' ')
                else:
                    print('-', end=' ')
            print()

game = WumpusWorld()

while True:
        game.print_grid()
        print(game.check_agent_status())

        if game.check_agent_status() != "You are safe.":
            break
        
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        game.move(move)
    
print("Game over.")
