##  Day 19: Graphs & BFS/DFS Traversals
from collections import deque
from operator import truediv


## Practice Question  #1 ##
# Create a graph using an adjacency list and write a function to print all nodes using BFS.

def bfs(graph, startNode):
    visited = set()
    queue = deque([startNode])
    while queue:
        node = queue.popleft()
        if node  not in visited:
            print(node)
            visited.add(node)
            queue.extend( neighbour for neighbour in graph[node] if neighbour not in visited )

#Practice Question #2
# Write a function to detect whether a path exists between two nodes in a graph using DFS.

def path_exists(graph, startNode, EndNode, visited=None):
    if startNode == EndNode:
        return  True
    else:
        if visited is None:
            visited = set()
        if startNode  in visited:
                return False
        visited.add(startNode)
        for neighbor in graph.get(startNode, []):
           if path_exists(graph, neighbor, EndNode, visited):
               return True
           else:
               return False

## Practice Question # 3
## Given a grid of islands and water, write a function that returns the total number of islands using BFS. ##





