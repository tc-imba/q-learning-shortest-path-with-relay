import src.dijkstra as dijkstra
import src.qlearning as qlearning

stations = 74
stations_id = []
for i in range(stations // 3):
    stations_id.append(i * 3 + 1)
stations_id.append(29)
fuel_max = 1

for i in range(1, stations + 1):
    for j in range(1, stations + 1):
        if i != j:
            p1, optimal = dijkstra.find_minimum_path('Eastern-Massachusetts', stations_id, i, j, fuel_max=fuel_max,
                                                     cost_bound=2, time_limit=2, alias='EMA')
            p2 = qlearning.find_minimum_path('Eastern-Massachusetts', stations_id, i, j, fuel_max=fuel_max,
                                             total_episodes=10000, alias='EMA')
            optimal_str = ''
            different_str = ''
            if not optimal:
                optimal_str = ' (not optimal)'
            if p1 != p2:
                different_str = ' (different)'
            result = '%d->%d: p1=%f%s, p2=%f%s' % (i, j, p1, optimal_str, p2, different_str)
            print(result)
