


def func_1(v,d):
    '''
    "v" is the initial node and d is the distance threshold

    '''

    # we are going to use a BFS algorithm with a distance

    # the visited list: if v[i] = True it means that the i-th node was visited by the algorithm
    vis = [False]*(len(g.nodes)+1)
    # this array will contain the distances of all visited nodes from the initial node "v"
    dist = [0]*(len(g.nodes)+1)

    v = 2
    # "q" is a queue
    q = []
    q.append(v)
    vis[v] = True
    # edges list
    edges = []

    '''
    Just standard BFS algorithm
    '''

    while q:
        s = q.pop()
        n = adj_list[s]
        for i in n:
            if vis[i] == False:
                tmp = int(g.edges[(s,i)]['dis']) + dist[s]
                if tmp <= d:
                    q.append(i)
                    edges.append((s,i))
                    vis[i]=True
                    dist[i]=tmp 


    '''
    subgraph making
    '''                        
    neigh = []
    # check the vis array and when the value is True add it in the list
    for i in range(len(vis)):
        if vis[i]==True:
            neigh.append(i)
    # subgraph making 
    subg = nx.Graph()
    # add nodes
    for x in neigh:
        subg.add_node(x, pos = g.nodes[x]['pos'])
    # add edges
    for x in edges:
        subg.add_edge(x[0], x[1], dis = g.edges[x]['dis'])

    return(subg)
