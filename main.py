import numpy as np
import pandas as pd
import random


class Node:
    def __init__(self, name, is_station):
        self.name = name
        self.is_station = is_station
        self.path = []


class Path:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
        self.Q = 0
        self.R = -cost


node = {}
path = []

node_df = pd.read_csv('node.csv', header=None)
for row in node_df.iterrows():
    name = row[1][0]
    is_station = row[1][1] == 1
    node[name] = Node(name, is_station)

path_df = pd.read_csv('path.csv', header=None)
for row in path_df.iterrows():
    start = node[row[1][0]]
    end = node[row[1][1]]
    cost = row[1][2]
    p = Path(start, end, cost)
    path.append(p)
    start.path.append(p)
    p = Path(end, start, cost)
    path.append(p)
    end.path.append(p)

total_episodes = 15000  # Total episodes
learning_rate = 0.8  # Learning rate
max_steps = 99  # Max steps per episode
gamma = 0.95  # Discounting rate

# Exploration parameters
epsilon = 1.0  # Exploration rate
max_epsilon = 1.0  # Exploration probability at start
min_epsilon = 0.01  # Minimum exploration probability
decay_rate = 0.005

start_node = node[1]
end_node = node[7]

for episode in range(total_episodes):
    total_rewards = 0
    station_passed = 0
    state = start_node  # The initial state should be the start node

    for step in range(max_steps):
        tradeoff = random.uniform(0, 1)
        if tradeoff > epsilon:
            # Exploitation (max Q in path)
            action = state.path[0]
            for p in state.path:
                if p.Q > action.Q:
                    action = p
        else:
            # Exploration (random Q in path)
            action = state.path[random.randint(0, len(state.path) - 1)]

        new_state = action.end
        reward = action.R
        done = action.end == end_node

        if new_state.is_station:
            station_passed += 1

        if done:
            if station_passed < 1:
                reward -= 100
            else:
                reward += 10

        total_rewards += reward
        new_state_Q = new_state.path[0].Q
        for p in new_state.path:
            if p.Q > new_state_Q:
                new_state_Q = p.Q
        action.Q += learning_rate * (reward + gamma * new_state_Q - action.Q)

        state = new_state

        if done:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)


state = start_node
for i in range(10):
    action = state.path[0]
    for p in state.path:
        if p.Q > action.Q:
            action = p
    print(action.start.name, action.end.name, action.cost, action.Q)
    state = action.end
    if state == end_node:
        break

