import math
import pandas as pd
import random

fuel_tank_divisions = 5


class Node:
    def __init__(self, id: int):
        self.id = id
        self.is_station = False
        self.flow = {}
        self.states = []
        self.paths = []
        for i in range(fuel_tank_divisions):
            self.states.append(State(self, i))
        self.state_fail = State(self, -1)

    def add_flow(self, term_node, flow: float):
        self.flow[term_node.id] = flow

    def add_path(self, path):
        for i in range(fuel_tank_divisions):
            self.states[i].add_path(path)
        self.paths.append(path)


class Path:
    def __init__(self, init_node: Node, term_node: Node,
                 capacity: float, free_flow_time: float, B: float, power: float):
        self.a = free_flow_time
        self.b = free_flow_time * B / (capacity ** power)
        self.flow = init_node.flow[term_node.id]
        self.cost = self.a + self.b * self.flow
        self.init_node = init_node
        self.term_node = term_node


class State:
    def __init__(self, node: Node, fuel_rank_state: int):
        self.node = node
        self.fuel_rank_state = fuel_rank_state
        self.paths = []

    def add_path(self, path: Path):
        actions = []
        for i in range(fuel_tank_divisions):
            actions.append(Action(path.term_node.states[i], path))
        # Fail Action
        actions.append(Action(path.term_node.state_fail, path))
        self.paths.append((path, actions))

    def get_available_actions(self, fuel_current, fuel_total):
        available_actions = []
        for (path, actions) in self.paths:
            if fuel_current >= path.cost:
                if path.term_node.is_station:
                    fuel_rank_state_new = fuel_tank_divisions - 1
                else:
                    fuel_rank_state_new = math.floor((fuel_current - path.cost) / fuel_total * fuel_tank_divisions)
                available_actions.append(actions[fuel_rank_state_new])
            else:
                # Fail Action
                available_actions.append(actions[fuel_tank_divisions])
        return available_actions

    def get_best_action(self, fuel_current, fuel_total):
        actions = self.get_available_actions(fuel_current, fuel_total)
        action = actions[0]
        for i in range(1, len(actions)):
            if actions[i].Q > action.Q:
                action = actions[i]
        return action

    def get_random_action(self, fuel_current, fuel_total):
        actions = self.get_available_actions(fuel_current, fuel_total)
        return actions[random.randint(0, len(actions) - 1)]


class Action:
    def __init__(self, new_state: State, path: Path):
        self.new_state = new_state
        self.R = -path.cost
        self.Q = 0


class SearchState:
    def __init__(self, prev_state, node: Node, total_cost: float, fuel_current: float):
        self.prev_state = prev_state
        self.node = node
        self.total_cost = total_cost
        self.fuel_current = fuel_current


def load_data(stations_id: list):
    nodes = {}
    paths = []

    def ensure_node(id):
        id = int(id)
        if id not in nodes:
            nodes[id] = Node(id)
        return nodes[id]

    trips_df = pd.read_excel('SiouxFalls_trips.xlsx', header=None)
    init_node_id = 0
    init_node = None
    for row in trips_df.iterrows():
        if row[1][0] == 'Origi':
            init_node_id += 1
            init_node = ensure_node(init_node_id)
            continue
        if init_node:
            for i in range(len(row[1]) // 2):
                term_node_id = row[1][2 * i]
                if math.isnan(term_node_id):
                    break
                term_node = ensure_node(term_node_id)
                init_node.add_flow(term_node, float(row[1][2 * i + 1]))

    net_df = pd.read_excel('SiouxFalls_net.xlsx', header=0)
    for row in net_df.iterrows():
        init_node = ensure_node(int(row[1][1]))
        term_node = ensure_node(int(row[1][2]))
        capacity = float(row[1][3])
        free_flow_time = float(row[1][5])
        B = float(row[1][6])
        power = float(row[1][7])
        path = Path(init_node, term_node, capacity / 1000, free_flow_time, B, power)
        init_node.add_path(path)
        paths.append(path)

    # Set the stations
    for id in stations_id:
        assert id in nodes
        nodes[id].is_station = True

    return nodes, paths
