from py2opt.routefinder import RouteFinder

nodes = ['1', '2', '3', '4', '5']

node1_weights = [0, 2, 1, 7, 4]
node2_weights = [2, 0, 3, 5, 3]
node3_weights = [1, 3, 0, 3, 2]
node4_weights = [7, 5, 3, 0, 4]
node5_weights = [4, 3, 2, 4, 0]

weight = [node1_weights, node2_weights, node3_weights, node4_weights, node5_weights]
route_finder = RouteFinder(weight, nodes, iterations=1000000, return_to_begin=True)
min_weight, best_route = route_finder.solve()

print(min_weight)
print(best_route)
