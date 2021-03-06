import numpy as np
import random

from src.base import load_data, fuel_tank_divisions


def find_minimum_path(network, stations_id, start_id, end_id, fuel_max=12., total_episodes=10000, silent=True,
                      alias=None, station_cost=1.):
    nodes, paths = load_data(network, stations_id, alias=alias, station_cost=station_cost)

    # Set the Max Fuel
    # fuel_max = 12

    # Find the shortest path from 1 to 24
    assert start_id in nodes
    assert end_id in nodes
    start_node = nodes[start_id]
    end_node = nodes[end_id]

    # Q Learning parameters
    # total_episodes = 1500  # Total episodes
    learning_rate = 0.8  # Learning rate
    max_steps = 99 * len(nodes)  # Max steps per episode
    gamma = 0.95  # Discounting rate

    # Exploration parameters
    epsilon = 1.0  # Exploration rate
    max_epsilon = 1.0  # Exploration probability at start
    min_epsilon = 0.01  # Minimum exploration probability
    decay_rate = 0.005

    def find_path(min_total_cost, learn=True):

        # The initial state should be max fuel
        fuel_current = fuel_max
        total_reward = 0
        state = start_node.states[fuel_tank_divisions - 1]
        passed_nodes = {}

        for step in range(max_steps):
            tradeoff = random.uniform(0, 1)
            if not learn or tradeoff > epsilon:
                # Exploitation (max Q in path)
                action = state.get_best_action(fuel_current, fuel_max, passed_nodes)
            else:
                # Exploration (random Q in path)
                action = state.get_random_action(fuel_current, fuel_max)

            # if not action:
            #     break

            new_state = action.new_state
            reward = action.R
            done = new_state.node == end_node

            total_reward += reward
            if new_state.fuel_rank_state >= 0 and action.is_station:
                fuel_current = fuel_max
                assert new_state.fuel_rank_state == fuel_tank_divisions - 1
            else:
                fuel_current += action.R  # action.R = -path.cost

            if new_state.node.id not in passed_nodes:
                passed_nodes[new_state.node.id] = fuel_current
            else:
                passed_nodes[new_state.node.id] = max(fuel_current, passed_nodes[new_state.node.id])

            if learn:
                if new_state.fuel_rank_state < 0:
                    assert fuel_current < 0
                    new_state_Q = -fuel_max * 5
                else:
                    new_state_action = new_state.get_best_action(fuel_current, fuel_max, passed_nodes)
                    # if not new_state_action:
                    #     break
                    new_state_Q = new_state_action.Q
                action.Q += learning_rate * (reward + gamma * new_state_Q - action.Q)
            elif not silent:
                print('%d->%d,fuel=%f,R=%f,Q=%f,station=%d' % (state.node.id, new_state.node.id, fuel_current,
                                                               action.R, action.Q, action.is_station))

            if -total_reward >= min_total_cost:
                break

            if new_state.fuel_rank_state < 0:
                if not learn:
                    print('No Fuel')
                break

            state = new_state
            if done:
                min_total_cost = -total_reward
                break

        if not learn and not silent:
            print('total cost: %f' % -total_reward)

        return min_total_cost

    min_total_cost = float('inf')

    for episode in range(total_episodes):
        min_total_cost = find_path(min_total_cost, True)
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

    return find_path(min_total_cost, False)


if __name__ == '__main__':
    find_minimum_path('Eastern-Massachusetts', [5, 11, 13, 18], 1, 69, fuel_max=0.8, silent=False, alias='EMA',
                      station_cost=0.2)
