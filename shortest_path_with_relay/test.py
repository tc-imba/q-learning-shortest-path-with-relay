import shortest_path_with_relay.dijkstra as dijkstra
import shortest_path_with_relay.qlearning as qlearning

stations_id = [5, 11, 13, 18]
fuel_max = 12

for i in range(1, 25):
    for j in range(1, 25):
        if i != j:
            p1 = dijkstra.find_minimum_path(stations_id, i, j, fuel_max=fuel_max)
            p2 = qlearning.find_minimum_path(stations_id, i, j, fuel_max=fuel_max, total_episodes=1500)
            if p1 == p2:
                print('correct in %d->%d,p=%f' % (i, j, p1))
            else:
                print('error in %d->%d,p1=%f,p2=%f' % (i, j, p1, p2))
