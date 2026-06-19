import numpy as np

class GridEnvironment:

    def __init__(self, size=10):

        self.size = size

        self.start = (0, 0)
        self.goal = (9, 9)

        self.hazards = []
        self.obstacles = []

        self.reset()

    def reset(self):

        self.agent_pos = self.start
        return self.agent_pos


    def step(self, action):

        x, y = self.agent_pos

        # Move agent
        if action == 0:   # up
            x -= 1
        elif action == 1: # down
            x += 1
        elif action == 2: # left
            y -= 1
        elif action == 3: # right
            y += 1

        # Boundary check
        x = max(0, min(self.size - 1, x))
        y = max(0, min(self.size - 1, y))

        # Obstacle check (stay in place)
        if (x, y) in self.obstacles:
            x, y = self.agent_pos

        self.agent_pos = (x, y)

        # Default reward
        reward = -1
        cost = 0
        done = False

        # Hazard (unsafe)
        if self.agent_pos in self.hazards:
            reward = -10
            cost = 1   # 🔥 Safety cost

        # Goal reached
        if self.agent_pos == self.goal:
            reward = 50
            done = True

        return self.agent_pos, reward, cost, done