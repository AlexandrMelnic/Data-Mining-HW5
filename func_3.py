# modified Fibonacci_Heap_Mod
# We modified it to keep track of the  nodes
from fibonacci_heap import Fibonacci_heap



# get the weight from the graph
# with a given modality
def get_weight(graph, node, next_node, mode):
    if mode == 'n':
        return 1
    elif mode == 't':
        return graph.get_edge_data(node, next_node)['time']
    elif mode == 'm':
        return graph.get_edge_data(node, next_node)['distance']


# Calculates the shortest path between two nodes
def dijkstra(graph, start, dest, mode):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    # initialize it with the initial node and set it with wight 0
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()
    
    # create a fibonacci heap and store the nodes
    # ordered by currend wight
    heap = Fibonacci_heap()
    
    while current_node != dest:
        # Add current node to the set of visited nodes
        visited.add(current_node)
        # adjacency list, take all edges from the current node
        destinations = [elem[1] for elem in graph.edges(current_node)]
        # take the total weight
        weight_to_current_node = shortest_paths[current_node][1]

        # visit all nodes connected to the current node
        for next_node in destinations:
            # calculate the weight of the current edge
            # weight of the edge + weight of edges previously visited in the path
            weight = get_weight(graph, current_node, next_node, mode) + weight_to_current_node
            
            # add nodes to the heap
            if next_node not in visited and next_node not in heap.nodes:
                heap.enqueue(next_node, weight)
            
            # add new node in shortest path
            # or update it if current path is shorter of previous path
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        # if heap is empty we cannot continue
        # and we cannot reach the destination
        
        if not heap.__bool__():
            return "Not Possible"
        
        # update current_node
        # next node is the destination with the lowest weight
        current_node = heap.dequeue_min().m_elem
    
    # Work back through destinations in shortest path
    # create path and reverse it
    path = []
    while current_node is not None:
        path.append(current_node)
        # take previous node from the dict
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return (path, shortest_paths[path[-1]][1])



# takes in input the starting node
# and then visit in order the list route
def shortest_ordered_route(graph, start, route, mode):
    if len(route) < 1:
        print("Insert at least 1 node")
        return
    total = 0
    path = [start]
    for elem in route:
        tmp = dijkstra(G, start, elem, mode)
        total += tmp[1]
        path.extend(tmp[0][1:])
        start = elem
    all_route = []
    all_route.extend([start])
    all_route.extend(route)
    return (path, all_route, total)
