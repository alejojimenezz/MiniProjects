from collections import deque

class graphModel:
    def __init__(self, V):

        self.V = V
        self.graph = {i: [] for i in range(1, V+1)}

    def addEdge(self, u , v, weigth=1):
        
        self.graph[u].append((v, weigth))
        self.graph[v].append((u, weigth))

    # BFS
    def bfs(self, start, objective):
        visited = set()
        tail = deque([(start, [start])])

        while tail:
            node, path = tail.popleft()
            if node == objective:
                return path
            if node not in visited:
                visited.add(node)
                for neighbour, i in self.graph.get(node, []):
                    if neighbour not in visited:
                        tail.append((neighbour, path + [neighbour]))
        
        return None
    
V = int(input("Ingerse el número de vertices: "))
E = int(input("Ingerse el número de aristas: "))
graph = graphModel(V)

for i in range(E):
    u = int(input("Ingrese valor de arista u: "))
    v = int(input("Ingrese valor de arista vecina de la anterior u (v): "))
    graph.addEdge(u, v)

s = int(input("Ingrese el nodo de origen: "))
t = int(input("Ingrese el nodo de destino: "))

route = graph.bfs(s, t)

if len(route) != 0:
    print("Done")