import numpy as np
import random

class QLearningAgent:

    def __init__(self, size=10):

        self.size = size
        self.actions = 4

        self.q_table = np.zeros((size,size,self.actions))

        self.lr = 0.1
        self.gamma = 0.95

        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

        self.episode_rewards = []


    def choose_action(self,state):

        x,y = state

        if random.random() < self.epsilon:
            return random.randint(0,3)

        return np.argmax(self.q_table[x,y])


    def update(self,state,action,reward,next_state):

        x,y = state
        nx,ny = next_state

        best_next = np.max(self.q_table[nx,ny])

        old = self.q_table[x,y,action]

        new_value = old + self.lr * (
            reward + self.gamma * best_next - old
        )

        self.q_table[x,y,action] = new_value

        return new_value


    def decay(self):

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay