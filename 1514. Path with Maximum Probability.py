# Soln using dijkstra
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create an adjacency list
        adj_list = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            adj_list[u].append((v, prob))
            adj_list[v].append((u, prob))
        
        # Priority queue to store (-probability, node)
        pq = [(-1.0, start_node)]
        prob_arr = [0.0] * n
        prob_arr[start_node] = 1.0
        
        while pq:
            # Get the node with the highest probability (note: we use -probability)
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob  # Convert back to positive probability

            if node == end_node:
                return curr_prob
            
            # Explore neighbors
            for neighbor, edge_prob in adj_list[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob_arr[neighbor]:
                    prob_arr[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0