# The following links are used to create the graph.
# https://www.educative.io/answers/how-to-implement-a-graph-in-python
# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
# https://experiencestack.co/graph-implementation-in-python-916fc3b6a8a
# For the DFS implementation, I have used the following link to detect a cycle, which gave me the pseudocode down below,
# DFS (Graph g, node u):
#         mark u as visited
#         for neighbors adj_node of u in Graph G:
#             if adj_node is not visited:
#                 DFS (G, adj_node).
# https://www.interviewkickstart.com/learn/depth-first-search-algorithm

def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

def add_edge(graph, v1, v2):
    if v1 in graph:
        graph[v1].append(v2)

def print_graph(graph):
    for vertex in graph:
        print(f"{vertex} -> {' '.join(map(str, graph[vertex]))}")

def detectCycleUtil(graph, current, origin, visited):
    if current in visited:
        return current == origin

    visited.add(current)
    for neighbour in graph[current]:
        if detectCycleUtil(graph, neighbour, origin, visited):
            return True
    return False

def isInCycle(match_scores, donor_friends, query):
    number_of_requests = len(match_scores[0])
    graph = {}

    for n in range(number_of_requests):
        add_vertex(graph, n)

    for donor_index, request_index in enumerate(donor_friends):
        for potential_request in range(number_of_requests):
            if match_scores[donor_index][potential_request] > 60:
                add_edge(graph, request_index, potential_request)

    visited = set()
    return detectCycleUtil(graph, query, query, visited)


def take_input():
    n = int(input())
    m = int(input())
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []
    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    print(isInCycle(match_scores, donor_friends, query))


take_input()
