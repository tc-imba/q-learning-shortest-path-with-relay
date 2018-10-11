import numpy as np
import pandas as pd
import random

stations_required = 1


class Node:
    def __init__(self, name, is_station: bool):
        self.name = name
        self.is_station = is_station
        # self.path = []
        self.states = []
        for i in range(stations_required + 1):
            self.states.append(State(self, i))

    def add_path(self, p):
        # self.path.append(p)
        for i in range(stations_required + 1):
            self.states[i].add_action(p)


class Path:
    def __init__(self, start: Node, end: Node, cost: int):
        self.start = start
        self.end = end
        self.cost = cost


class State:
    def __init__(self, node: Node, stations_count: int):
        self.node = node
        self.stations_count = stations_count
        self.actions_normal = []
        self.actions_add_station = []

    def add_action(self, p: Path):
        if self.stations_count < stations_required and p.end.is_station:
            self.actions_add_station.append(Action(p.end.states[self.stations_count + 1], p))
        self.actions_normal.append(Action(p.end.states[self.stations_count], p))

    def get_available_actions(self, stations_passed):
        actions = [] + self.actions_normal
        for action in self.actions_add_station:
            if len(stations_passed) < stations_required and action.new_state.node not in stations_passed:
                actions.append(action)
        return actions

    def get_best_action(self, stations_passed):
        actions = self.get_available_actions(stations_passed)
        action = actions[0]
        for i in range(1, len(actions)):
            if actions[i].Q > action.Q:
                action = actions[i]
        return action

    def get_random_action(self, stations_passed):
        actions = self.get_available_actions(stations_passed)
        return actions[random.randint(0, len(actions) - 1)]


class Action:
    def __init__(self, new_state, path: Path):
        self.new_state = new_state
        self.R = -path.cost
        self.Q = 0


def __main__():
    total_episodes = 15000  # Total episodes
    learning_rate = 0.8  # Learning rate
    max_steps = 99  # Max steps per episode
    gamma = 0.95  # Discounting rate

    # Exploration parameters
    epsilon = 1.0  # Exploration rate
    max_epsilon = 1.0  # Exploration probability at start
    min_epsilon = 0.01  # Minimum exploration probability
    decay_rate = 0.005

    node = {}

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
        start.add_path(p)
        p = Path(end, start, cost)
        end.add_path(p)

    start_node = node[1]
    end_node = node[7]

    def find_path(learn=True):
        # The initial state should be the start node with no station passed
        stations_passed = set()
        state = start_node.states[len(stations_passed)]

        for step in range(max_steps):
            tradeoff = random.uniform(0, 1)
            if not learn or tradeoff > epsilon:
                # Exploitation (max Q in path)
                action = state.get_best_action(stations_passed)
            else:
                # Exploration (random Q in path)
                action = state.get_random_action(stations_passed)

            new_state = action.new_state
            reward = action.R
            done = new_state.node == end_node and new_state.stations_count >= stations_required

            if new_state.node.is_station and new_state.node not in stations_passed:
                stations_passed.add(new_state.node)

            if learn:
                new_state_Q = new_state.get_best_action(stations_passed).Q
                action.Q += learning_rate * (reward + gamma * new_state_Q - action.Q)
            else:
                print('%d->%d,Station=%d,R=%d,Q=%f' % (state.node.name, new_state.node.name,
                                                       len(stations_passed), action.R, action.Q))

            state = new_state
            if done:
                break

    for episode in range(total_episodes):
        find_path(True)
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

    find_path(False)


__main__()
