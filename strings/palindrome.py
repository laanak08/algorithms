# case = 'cba'

# letters = []
# s = list(case)
# transforms = 0
# start_repeat_index = -1

# if (len(s) % 2) == 0:
#     start_repeat_index = (len(s) / 2)
#     gain_pattern_index = start_repeat_index
# else:
#     start_repeat_index = (len(s)+1) / 2
#     gain_pattern_index = start_repeat_index - 1

# for k in range(0,len(s)):
#     c = s[k]
#     if k >= start_repeat_index:
#         if c == letters[-1]:
#             letters.pop()
#         else:
#             transform_distance = 0
#             dist_to_repeat_letter = abs(ord(c) - ord(letters[-1]))
#             dist_to_repeat_a = abs(ord(c) - ord('a'))
#             print dist_to_repeat_letter
#             print dist_to_repeat_a
#             if dist_to_repeat_letter > dist_to_repeat_a:
#                 transform_distance = dist_to_repeat_a
#             else:
#                 transform_distance = dist_to_repeat_letter
#             transforms += transform_distance
#             letters.pop()
    
#     elif k < gain_pattern_index:
#         letters.append(c)

# # print transforms

def dijkstra1(graph,startNode):
    # create list, considering all vertices as unvisited
    unvisitedVertices, distToVertex, prevPathToVertex = graph.keys(), {}, {}
    # initialize distances to each vertex at Infinity
    # consider all paths to each vertex as unknown
    for v in graph:
        distToVertex[v], prevPathToVertex[v] = INFINITY, ''
    # distance to starting node is always 0
    distToVertex[startNode] = 0
    # for all unvisited nodes
    while len(unvisitedVertices) > 0:
        # choose unvisited node from unanalyzed distance list with smallest visit cost
        currentVertex = min({key:value for key,value in distToVertex.items() if key in unvisitedVertices}, key=distToVertex.get)
        # mark chosen node as visited
        unvisitedVertices.remove(currentVertex)
        # analyze cost of visiting each neighbor node, using graph to determine current vertex's neighbors and their actual visit costs
        for neighborNode in graph[currentVertex]:
            neighbor, cost = neighborNode[0], neighborNode[1]
            # distance to current neighbor = distance to current node + cost of visiting neighbor
            updatedDistance = distToVertex[currentVertex] + cost
            # update if calculated distance is smaller than we've seen
            if updatedDistance < distToVertex[neighbor]:
                distToVertex[neighbor] = updatedDistance
                prevPathToVertex[neighbor] = currentVertex
    return distToVertex


import Queue

def dijkstra2(graph,startNode):
    unvisitedVertices, distToVertex, prevPathToVertex = Queue.PriorityQueue(), {}, {}
    distToVertex[startNode] = 0
    for v in graph:
        if v != startNode:
            distToVertex[v], prevPathToVertex[v] = INFINITY, ''
        unvisitedVertices.put((distToVertex[v],v))
    while not unvisitedVertices.empty():
        currentVertex = unvisitedVertices.get_nowait()[1]
        for neighborNode in graph[currentVertex]:
            neighbor, cost = neighborNode[0], neighborNode[1]
            updatedDistance = distToVertex[currentVertex] + cost
            if updatedDistance < distToVertex[neighbor]:
                distToVertex[neighbor] = updatedDistance
                prevPathToVertex[neighbor] = currentVertex
                unvisitedVertices.put_nowait((updatedDistance,neighbor))
    return distToVertex

INFINITY = float("inf")
UNREACHABLE = -1
for caseNum in range(0,int(raw_input())):
    numNodes, numEdges = raw_input().split(' ')
    graph = {}
    for v in range(0,int(numNodes)):
        graph[v+1] = []

    for e in range(0,int(numEdges)):
        v1, v2, cost = raw_input().split(' ')
        graph[int(v1)].append((int(v2),int(cost)))
        graph[int(v2)].append((int(v1),int(cost)))

    startNode = int(raw_input())
    dist = dijkstra2(graph,startNode)

    costs = []
    for node, cost in dist.items():
        if node != startNode:
            if cost == INFINITY:
                cost = UNREACHABLE
            costs.append(cost)
    print ' '.join([str(elem) for elem in costs])