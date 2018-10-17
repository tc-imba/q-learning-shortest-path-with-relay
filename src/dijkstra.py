from src.base import load_data, Path, SearchState
import queue


def find_minimum_path(network, stations_id, start_id, end_id, fuel_max=12, silent=True):
    nodes, paths = load_data(network, stations_id)

    # Set the Max Fuel
    # fuel_max = 12

    # Find the shortest path from 1 to 24
    assert start_id in nodes
    assert end_id in nodes
    start_node = nodes[start_id]
    end_node = nodes[end_id]

    min_total_cost = float('inf')
    min_search_state = None

    X = queue.Queue()
    X.put(SearchState(None, Path(start_node, start_node), 0, fuel_max))

    while not X.empty():
        state_current = X.get()
        if state_current.total_cost >= min_total_cost:
            continue
        node_current = state_current.path.term_node
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
            new_state = SearchState(state_current, path, total_cost, fuel_current)
            # success if reaches the end
            if path.term_node == end_node:
                min_total_cost = total_cost
                min_search_state = new_state
            else:
                X.put(new_state)

    def print_path(search_state: SearchState):
        if search_state.prev_state:
            print_path(search_state.prev_state)
            path = search_state.path
            print('%d->%d,fuel=%f,R=%f' % (path.init_node.id, path.term_node.id,
                                           search_state.fuel_current, -path.cost))

    if not silent:
        print_path(min_search_state)
        print('total cost: %f' % min_total_cost)

    return min_total_cost


if __name__ == '__main__':
    find_minimum_path('SiouxFalls', [5, 11, 13, 18], 1, 20, fuel_max=12, silent=False)
