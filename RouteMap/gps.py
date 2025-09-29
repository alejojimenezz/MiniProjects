'''
Little GPS / Route planner project
Graph and algorithms practice
BFS / DFS / Dijkstra
'''

from collections import deque
import heapq

class Graph:
    def __init__(self):

        self.graph = {}

    def add_edge(self, u , v, weigth=1):
        
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weigth))
        self.graph[v].append((u, weigth))

    # BFS
    def bfs(self, start, objective):
        visited = set()
        tail = deque([start, [start]])

        while tail:
            node, path = tail.popleft()
            if node == objective:
                return path
            if node not in visited:
                visited.add(node)
                for neighbour, _ in self.graph.get(node, []):
                    if neighbour not in visited:
                        tail.append((neighbour, path + [neighbour]))
        
        return None
    
    # DFS
    def dfs(self, start, objective):
        visited = set()
        stack = [(start, [start])]

        while stack:
            node, path = stack.pop()
            if node == objective:
                return path
            if node not in visited:
                visited.add(node)
                for neighbour, _ in self.graph.get(node, []):
                    if neighbour not in visited:
                        stack.append((neighbour, path + [neighbour]))
        
        return None