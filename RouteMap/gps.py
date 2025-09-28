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
        pass