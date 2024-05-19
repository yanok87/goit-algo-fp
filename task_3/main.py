"""Dijkstra's algorithm to find the shortest paths in a weighted graph using a binary heap"""

import heapq


class Graph:
    """Creation of graph"""

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        """Add edges to graph"""
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # For undirected graph

    def dijkstra(self, src):
        """Dijkstra algorythm to find the shortest path"""
        # Priority queue to store vertices
        pq = []
        # Create a list to hold distances, initialized with infinity
        dist = [float("inf")] * self.vertices
        # Set distance of source vertex to itself as 0
        dist[src] = 0
        # Push the source vertex into priority queue
        heapq.heappush(pq, (0, src))

        while pq:
            # Extract the minimum distance vertex from priority queue
            distance, u = heapq.heappop(pq)

            # Traverse through all adjacent vertices of u
            for v, weight in self.graph[u]:
                # If there is a shorter path to v through u
                if dist[u] + weight < dist[v]:
                    # Update distance of v
                    dist[v] = dist[u] + weight
                    # Push v into priority queue with updated distance
                    heapq.heappush(pq, (dist[v], v))

        # Print shortest distances from source
        print("Vertex\tDistance from Source")
        for i in range(self.vertices):
            print(f"{i}\t{dist[i]}")


# Example usage:
# Create a graph
g = Graph(9)
# Add edges and weights
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

# Find shortest paths from source vertex 0
g.dijkstra(0)
