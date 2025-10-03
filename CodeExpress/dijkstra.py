import heapq

class graphModel:
    def __init__(self):

        self.graph = {}

    def addEdge(self, u , v, weigth=1):
        
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weigth))
        self.graph[v].append((u, weigth))
    
    # Dijkstra
    def dijkstra(self, start, objective):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        tail = [(0, start, [start])]
        visited = set()

        while tail:
            distance, node, path = heapq.heappop(tail)
            if node in visited:
                continue
            visited.add(node)

            if node == objective:
                return distance, path
            
            for neighbour, weigth in self.graph[node]:
                if neighbour not in visited:
                    new_dist = distance + weigth
                    if new_dist < distances[neighbour]:
                        distances[neighbour] = new_dist
                        heapq.heappush(tail, (new_dist, neighbour, path + [neighbour]))
            
        return float("inf"), []
    
if __name__ == "__main__":

    g = graphModel()
    g.addEdge("Bogota", "Medellín", 420)
    g.addEdge("Bogota", "Cali", 460)
    g.addEdge("Medellín", "Cartagena", 640)
    g.addEdge("Cali", "Pasto", 400)
    g.addEdge("Cali", "Medellín", 415)

    print("Dijkstra (ruta más corta en distancia)", g.dijkstra("Bogota", "Pasto"))