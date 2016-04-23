import Queue

INFINITY = float("inf")
UNREACHABLE = -1

def run():
    numNodes, numEdges = raw_input().split(' ')
    graph = {}
    for v in range(0,int(numNodes)):
        graph[v+1] = []

    for e in range(0,int(numEdges)):
        v1, v2, cost = raw_input().split(' ')
        graph[int(v1)].append((int(v2),int(cost)))
        graph[int(v2)].append((int(v1),int(cost)))

    startNode = int(raw_input())
    costs, path = prim(graph,startNode)
    print sum(costs.values())

def prim(graph,startNode):
    unvisited, costs, path = Queue.PriorityQueue(), {}, {}
    unvisited_set = set([])

    costs[startNode] = 0
    for v in graph.keys():
        if v != startNode:
            costs[v], path[v] = INFINITY, ''
        unvisited.put_nowait((costs[v],v))
        unvisited_set.add(v)

    while not unvisited.empty():
        currentNode = unvisited.get_nowait()[1]
        
        if currentNode in unvisited_set:
            unvisited_set.remove(currentNode)

        for neighbor in graph[currentNode]:
            node, cost = neighbor[0], neighbor[1]
            if node in unvisited_set and cost < costs[node]:
                costs[node] = cost
                path[node] = currentNode
                unvisited.put_nowait((costs[node],node))

    return costs, path

run()


# from pythonds.graphs import PriorityQueue, Graph, Vertex

# def prim(G,start):
#     pq = PriorityQueue()
#     for v in G:
#         v.setDistance(sys.maxsize)
#         v.setPred(None)
#     start.setDistance(0)
#     pq.buildHeap([(v.getDistance(),v) for v in G])
#     while not pq.isEmpty():
#         currentVert = pq.delMin()
#         for nextVert in currentVert.getConnections():
#           newCost = currentVert.getWeight(nextVert)
#           if nextVert in pq and newCost<nextVert.getDistance():
#               nextVert.setPred(currentVert)
#               nextVert.setDistance(newCost)
#               pq.decreaseKey(nextVert,newCost)