from shortest_path_with_relay.base import load_data, Path, SearchState
import queue


def __main__(stations_id):
    nodes, paths = load_data(stations_id)

    # Set the Max Fuel
    fuel_max = 12

    # Find the shortest path from 1 to 24
    start_node = nodes[1]
    end_node = nodes[20]

    min_total_cost = float('inf')
    min_search_state = None

    X = queue.Queue()
    X.put(SearchState(None, start_node, 0, fuel_max))

    while not X.empty():
        state_current = X.get()
        if state_current.total_cost >= min_total_cost:
            continue
        node_current = state_current.node
        for path in node_current.paths:
            # fail when fuel is not enough
            if state_current.fuel_current < path.cost:
                continue

            # fail when total cost exceeds the local minimum
            total_cost = state_current.total_cost + path.cost
            if total_cost >= min_total_cost:
                continue

            # add fuel if next node is a station
            if path.term_node.is_station:
                fuel_current = fuel_max
            else:
                fuel_current = state_current.fuel_current - path.cost

            new_state = SearchState(state_current, path.term_node, total_cost, fuel_current)
            # success if reaches the end
            if path.term_node == end_node:
                min_total_cost = total_cost
                min_search_state = new_state
            else:
                X.put(new_state)

    def print_path(search_state: SearchState):
        if search_state.prev_state:
            print_path(search_state.prev_state)
            print('%d->%d,fuel=%f,total_cost=%f' % (search_state.prev_state.node.id, search_state.node.id,
                                                    search_state.fuel_current, search_state.total_cost))

    print_path(min_search_state)
    print('total cost: %f' % min_total_cost)


if __name__ == '__main__':
    __main__([5, 11, 13, 18])
